import tkinter as tk
import tkinter.messagebox as tkm

# ボタンがクリックされた時の挙動
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=": #「=」が押された時
        txt = entry.get() #入力欄の値を取得
        txt = txt.replace("÷", "/")
        txt = txt.replace("×", "*")
        ans = eval(txt) #入力欄の値を評価、計算
        entry.delete(0, tk.END) #入力欄の削除
        entry.insert(tk.END, ans) #計算結果を入力欄に戻す
    elif num == "AC":
        entry.delete(0, tk.END)
    elif num == "C":
        txt = entry.get() #入力欄の値を取得
        ans = txt[0:-1]
        entry.delete(0, tk.END) #入力欄の削除
        entry.insert(tk.END, ans) #計算結果を入力欄に戻す
    elif num == "±":
        txt = entry.get() #入力欄の値を取得
        try:
            ans = float(txt) * -1 #入力欄の値にマイナス１をかける
            entry.delete(0, tk.END) #入力欄の削除
            entry.insert(tk.END, ans) #計算結果を入力欄に戻す
        except:
            pass
    else: #上記以外のボタンが押された時
        #クリックしたボタンの値を入力欄の末尾に入れる
        entry.insert(tk.END, num)
def enter_bg(event): #マウスホバー時の処理
    event.widget['bg'] = "#808080"
def leave_bg(event): #マウスが離れた時の処理
    event.widget['bg'] = "#696969"


root = tk.Tk()
root.title("電卓") #タイトル
root.geometry("400x470") #ウィンドウサイズの設定
root.resizable(False, False)
root.configure(bg="black") #背景色の変更

#入力欄
entry = tk.Entry(root, justify="right", width=14, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=4)

r, c = 1, 0
count = 0
operators = [["AC", "C", "±", "÷"], ["×", "-", "+"], [".", "="]]
#数字のボタン
for ope in operators[0]:
    Button = tk.Button(root, text=f"{ope}", width=4, height=1, font=("Times New Roman", 30))
    Button.grid(row=r, column=c)
    Button.bind("<1>", button_click)
    c += 1
    if c%4 == 0:
        c = 0
r += 1

for num in range(9, -1, -1):
    if c==2:
        moji = operators[1][count]
        Button = tk.Button(root, text=f"{moji}", width=4, height=1, font=("Times New Roman", 30))
        Button.grid(row=r, column=(c+1))
        Button.bind("<1>", button_click)
        count += 1
    if num == 0:
        Button = tk.Button(root, text=f"{num}", width=8, height=1, font=("Times New Roman", 31), fg="white", bg="#696969")
        Button.grid(row=r, column=c, columnspan=2)
    else:
        Button = tk.Button(root, text=f"{num}", width=4, height=1, font=("Times New Roman", 30), fg="white", bg="#696969")
        Button.grid(row=r, column=c)
    Button.bind("<Enter>", enter_bg)
    Button.bind("<Leave>", leave_bg)
    Button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

#数字以外のボタン
for ope in operators[2]:
    Button = tk.Button(root, text=f"{ope}", width=4, height=1, font=("Times New Roman", 30))
    Button.grid(row=r, column=c+1)
    Button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()