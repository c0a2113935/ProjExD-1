import tkinter as tk
import tkinter.messagebox as tkm

def msg():
    tkm.showinfo("のボタン", "１のボタンがクリックされました。")

root = tk.Tk()
root.geometry("300x500")

r, c = 0, 0
for num in range(9, -1, -1):
    if c == 3:
        c = 0
        r += 1
    Button = tk.Button(root, text=f"{num}", command=msg, width=4, height=2, font=("Times New Roman", 30))
    Button.grid(row=r, column=c)
    c += 1


root.mainloop()