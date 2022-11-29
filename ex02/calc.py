import tkinter as tk
import tkinter.messagebox as tkm

def msg(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(f"{txt}のボタン", f"{txt}ボタンがクリックされました。")

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
for num in range(9, -1, -1):
    Button = tk.Button(root, text=f"{num}", width=4, height=2, font=("Times New Roman", 30))
    Button.grid(row=r, column=c)
    Button.bind("<1>", msg)
    c += 1
    if c%3 == 0:
        c = 0
        r += 1

root.mainloop()