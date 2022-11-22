import random
import time
count = 0
max = 5
taisyou_number = 10
kesson_number = 2

def alphabet_show():
    global count
    count += 1
    if count > max:
        print("最大繰り返し回数をオーバーしました。")
        return
    x = random.sample(range(65, 91), taisyou_number)
    taisyou_lst = []
    for i in x:
        taisyou_lst.append(chr(i))
    hyouji_lst = taisyou_lst.copy()
    taisyou_lst.sort()
    hyoji_lst = random.sample(hyouji_lst, (taisyou_number-kesson_number))
    kesson_lst = list(set(taisyou_lst) ^ set(hyoji_lst))
    print("対象文字：")
    print(" ".join(taisyou_lst))
    print("欠損文字（デバッグ用）：")
    print(" ".join(kesson_lst))
    print("表示文字：")
    print(" ".join(hyoji_lst))
    print()
    answer(kesson_lst)

def answer(kesson_lst):
    try:
        ans_number = int(input("欠損文字はいくつあるでしょうか？："))
    except:
        print("数字を入力してください。")
        fuseikai()
        return
    if ans_number == len(kesson_lst):
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        for i in range(len(kesson_lst)):
            ans_moji = input(str(i+1) + "つ目の文字を入力してください：")
            if ans_moji in kesson_lst:
                kesson_lst.remove(ans_moji)
            else:
                fuseikai()
                break
        else:
            print("大正解です")
    else:
        fuseikai()

def fuseikai():
    print("不正解です。またチャレンジしてください")
    print("-" * 20)
    alphabet_show()

if __name__ == "__main__":
    st = time.time()
    alphabet_show()
    ed = time.time()
    print(f"プログラムの実行に{(ed-st):.2f}秒かかりました")