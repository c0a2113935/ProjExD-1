import tkinter as tk
import tkinter.messagebox as tkm
import random
import maze_maker
from PIL import Image, ImageTk

# キーが押された時の処理
def key_down(event):
    global key
    key = event.keysym

#キーが離された時の処理
def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, index
    if key == "Up": # ↑ボタンが押されたら
        if maze_list[mx][my-1] == 0: #進む場所が床だったら
            cy -= 100
            my -= 1
    elif key == "Down": # ↓ボタンが押されたら
        if maze_list[mx][my+1] == 0:
            cy += 100
            my += 1
    elif key == "Left": # ←ボタンが押されたら
        if maze_list[mx-1][my] == 0:
            cx -= 100
            mx -= 1
    elif key == "Right": # →ボタンが押されたら
        if maze_list[mx+1][my] == 0:
            cx += 100
            mx += 1
    canvas.coords("kokaton", cx, cy)
    if kokaton_have == False:
        if mx == a and my == b: #つるはしと重なったら
            turuhasi() #つるはし関数の呼び出し
    if index==1: #こうかとんがつるはしを持ってる画像だったら
        if key == "space": #スペースが押されたら
            #つるはしで壁を破壊しようとした処理（未完成）
            if maze_list[mx+1][my] == 1: maze_list[mx+1][my] = 0
            elif maze_list[mx][my+1] == 1: maze_list[mx][my+1] = 0
            elif maze_list[mx][my-1] == 1: maze_list[mx][my-1] = 0
            elif maze_list[mx-1][my] == 1: maze_list[mx-1][my] = 0
            else:
                pass
            # こうかとんの画像を変更
            index = 2
            canvas.delete("kokaton")
            canvas.create_image(cx, cy, image=photos[index], tag="kokaton")
    
    # こうかとんがゴールと重なったら
    if mx==meiro_x-2 and my==meiro_y-2:
        if tkm.showinfo("おめでとう！", "ゴールにたどり着きました") == "ok":  # okが押されたら
            root.destroy() # ウィンドウを閉じる
    else:
        root.after(100, main_proc)
 
# つるはし関数
def turuhasi():
    global index, kokaton_have
    canvas.delete(item) #つるはし削除
    # こうかとんの画像を変更
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

    # こうかとんの画像を格納するリスト
    photos = [tk.PhotoImage(file="fig/8.png"), tk.PhotoImage(file="fig/turuhasi_bird.png"), tk.PhotoImage(file="fig/6.png")]
    kokaton_have = False  #こうかとんがつるはしを持っているか
    index = 0  #こうかとんの画像を指定するための変数
    mx, my = 1, 1
    cx = mx*100 + 50 #横座標
    cy = my*100 + 50 #縦座標
    a = random.randint(1, meiro_x-1)
    try:
        b = maze_list[a].index(0)
        # ランダムでつるはしが迷路に現れる（現れない時もある）
        img_turuhasi = tk.PhotoImage(file="fig/turuhasi.png")
        item = canvas.create_image(a*100+50, b*100+50, image=img_turuhasi, tag="turuhasi")
    except:
        pass

    # ゴールの表示
    img_goal = tk.PhotoImage(file="fig/goal.png")
    goal_item = canvas.create_image((meiro_x-2)*100+50, (meiro_y-2)*100+50, image=img_goal, tag="goal")

    # こうかとんの画像の描画
    canvas.create_image(cx, cy, image=photos[index], tag="kokaton")
    key = ""
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
