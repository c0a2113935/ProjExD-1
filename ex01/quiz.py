import random

number = random.randint(0, 2)

quiz_list = ["サザエの旦那の名前は？", "カツオの妹の名前は？", "タラオはカツオから見てどんな関係？"]
print("問題：")
print(quiz_list[number])
answer = input("答えを入力してください：")
quiz_answer = [["マスオ", "ますお"], ["ワカメ", "わかめ"], ["甥", "おい", "甥っ子", "おいっこ"]]
if answer in quiz_answer[number]:
    print("正解！！！")
else:
    print("不正解です･･･")
