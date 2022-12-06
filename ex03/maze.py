import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")

    cx = 300 #横座標
    cy = 400 #縦座標
    img = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=img, tag="kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    canvas.pack()
    root.mainloop()
