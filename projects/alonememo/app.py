from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('0.0.0.0', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    cards = list(db.cards.find({},{'_id':0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'cards':cards, 'msg':'GET 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
        url_receive = request.form['url_give']
        comment_receive = request.form['comment_give']

        # # url_receive로 클라이언트가 준 url 가져오기
        # print(request.form)
        # url_receive = request.form['url_give']
        # # coment_receive로 클라이언트가 준 coment 가져오기
        # comment_receive = request.form['comment_give']

		# 2. meta tag를 스크래핑하기
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')['content']
        og_title = soup.select_one('meta[property="og:title"]')['content']
        og_description = soup.select_one('meta[property="og:description"]')['content']

        # url_image = og_image['content']
        # url_title = og_title['content']
        # url_description = og_description['content']

		# 3. mongoDB에 데이터 넣기
        card = {
            'image': og_image,
            'title': og_title,
            'desc':og_description,
            'url': url_receive,
            'comment': comment_receive
        }

        # reviews에 review 저장하기
        db.cards.insert_one(card)
        # 성공 여부 & 성공 메시지 반환
        return jsonify({'result': 'success', 'msg':'정상적으로 삽입되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)