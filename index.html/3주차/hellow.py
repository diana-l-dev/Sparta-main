fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def count_fruits(name):
    count = 0
    for fruit in fruits:
        if fruit == name:
            count += 1
    return count

subak_count = count_fruits('수박')
print(subak_count)

apple_count = count_fruits('사과')
print(apple_count)