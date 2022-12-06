import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up":
        if maze_list[mx][my-1] == 0:
            cy -= 100
            my -= 1
    elif key == "Down":
        if maze_list[mx][my+1] == 0:
            cy += 100
            my += 1
    elif key == "Left":
        if maze_list[mx-1][my] == 0:
            cx -= 100
            mx -= 1
    elif key == "Right":
        if maze_list[mx+1][my] == 0:
            cx += 100
            mx += 1
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze_list)

    mx, my = 1, 1
    cx = mx*100 + 50 #横座標
    cy = my*100 + 50 #縦座標
    img = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=img, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
