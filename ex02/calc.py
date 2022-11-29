import tkinter as tk
import tkinter.messagebox as tkm

# ボタンがクリックされた時の挙動
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=": #「=」が押された時
        txt = entry.get() #入力欄の値を取得
        ans = eval(txt) #入力欄の値を評価、計算
        entry.delete(0, tk.END) #入力欄の削除
        entry.insert(tk.END, ans) #計算結果を入力欄に戻す
    else: #「=」以外のボタンが押された時
        #クリックしたボタンの値を入力欄の末尾に入れる
        entry.insert(tk.END, num)

root = tk.Tk()
root.geometry("300x600") #ウィンドウサイズの設定

#入力欄
entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
#数字のボタン
for num in range(9, -1, -1):
    Button = tk.Button(root, text=f"{num}", width=4, height=2, font=("Times New Roman", 30))
    Button.grid(row=r, column=c)
    Button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

#数字以外のボタン
operators = ["+", "="]
for ope in operators:
    Button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("Times New Roman", 30))
    Button.grid(row=r, column=c)
    Button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()