import tkinter as tk
import tkinter.messagebox as tkm
import random
import maze_maker
from PIL import Image, ImageTk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, index
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
    if kokaton_have == False:
        if mx == a and my == b: #つるはしと重なったら
            turuhasi()
    if index==1:
        if key == "space":
            if maze_list[mx+1][my] == 1: maze_list[mx+1][my] = 0
            elif maze_list[mx][my+1] == 1: maze_list[mx][my+1] = 0
            elif maze_list[mx][my-1] == 1: maze_list[mx][my-1] = 0
            elif maze_list[mx-1][my] == 1: maze_list[mx-1][my] = 0
            else:
                pass
            index = 2
            canvas.delete("kokaton")
            canvas.create_image(cx, cy, image=photos[index], tag="kokaton")
    
    if mx==meiro_x-2 and my==meiro_y-2:
        tkm.showinfo("おめでとう！", "ゴールにたどり着きました")
    else:
        root.after(100, main_proc)


def turuhasi():
    global index, kokaton_have
    canvas.delete(item) #つるはし削除
    index = 1
    canvas.delete("kokaton")
    canvas.create_image(cx, cy, image=photos[index], tag="kokaton")
    kokaton_have = True

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    meiro_x, meiro_y = 15, 9
    maze_list = maze_maker.make_maze(meiro_x, meiro_y)
    maze_maker.show_maze(canvas, maze_list)

    photos = [tk.PhotoImage(file="fig/8.png"), tk.PhotoImage(file="fig/turuhasi_bird.png"), tk.PhotoImage(file="fig/6.png")]
    kokaton_have = False
    index = 0
    mx, my = 1, 1
    cx = mx*100 + 50 #横座標
    cy = my*100 + 50 #縦座標
    a = random.randint(1, meiro_x-1)
    try:
        b = maze_list[a].index(0)
        # ランダムでつるはしが迷路に現れる
        img_turuhasi = tk.PhotoImage(file="fig/turuhasi.png")
        item = canvas.create_image(a*100+50, b*100+50, image=img_turuhasi, tag="turuhasi")
    except:
        pass

    # ゴールの表示
    img_goal = tk.PhotoImage(file="fig/goal.png")
    goal_item = canvas.create_image((meiro_x-2)*100+50, (meiro_y-2)*100+50, image=img_goal, tag="goal")


    canvas.create_image(cx, cy, image=photos[index], tag="kokaton")
    key = ""
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
