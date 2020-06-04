from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('0.0.0.0', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])

def saving():
    # name_receive로 클라이언트가 준 name 가져오기
    name_receive = request.form['name_give']
    # op_receive로 클라이언트가 준 op 가져오기
    op_receive = request.form['op_give']
    # address_receive로 클라이언트가 준 address 가져오기
    address_receive = request.form['address_give']
    # phone_receive로 클라이언트가 준 phone 가져오기
    phone_receive = request.form['phone_give']

    # DB에 삽입할 order 만들기
    order = {
       'name': name_receive,
       'op': op_receive,
       'address': address_receive,
       'phone': phone_receive
    }
    # orders에 order 저장하기
    db.orders.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/orders', methods=['GET'])
def listing():
    # 1. DB에서 order 정보 모두 가져오기
    orders = list(db.orders.find({},{'_id':0}))
    # 2. 성공 여부 & order 목록 반환하기
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)