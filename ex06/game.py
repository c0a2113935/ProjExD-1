import pygame as pg
import sys

# ステージリスト
syougai = [
    1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
    1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 
    0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0
    ]

jamp = False
jamp_high = 160
jamp_kakeru = 1/5
jamp_count = 0
y = 580

def jamp_chara(): # キャラクターのジャンプ関数
    global jamp, jamp_high, jamp_kakeru, y, jamp_count
    if jamp == True:
        jamp_count += 1
        y -= jamp_high
        jamp_high *= jamp_kakeru
        if jamp_count == 2:
            jamp_high *= -5
            jamp_kakeru = 100
        if y >= 580:
            y = 580
            jamp_kakeru = 1/5
            jamp_high = 160
            jamp_count = 0
            jamp = False
    else:
        jamp == False
        jamp_high = 160
        jamp_kakeru = 1/5
        jamp_count = 0
        y = 580
    return y


def main():
    global jamp, y
    pg.display.set_caption("ゲームタイトル（仮）")       # ゲームタイトル
    scrn_sfc = pg.display.set_mode((1920, 1060))        # 画面サイズ
    scrn_rct = scrn_sfc.get_rect()
    clock =pg.time.Clock()
    # 背景画像
    img_bg = [
        pg.image.load("ex06/bg.jpg"),
        pg.image.load("ex06/ana.jpg")
        ]
    #img_bg_rct = img_bg.get_rect()
    img_chara = [
        pg.image.load("ex06/human_1.png"),
        pg.image.load("ex06/human_2.png"),
        pg.image.load("ex06/human_3.png"),
        pg.image.load("ex06/human_4.png")
    ]
    chara_live = True   # キャラクターの生存判定
    tmr = 0
    count = 0

    while True:
        tmr = tmr + 1
        #scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:       # 終了ボタン
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:    # エスケープを押すと終了
                    return
                if event.key == pg.K_F1:    # F1を押すとフルスクリーン
                    screen = pg.display.set_mode((1920, 1060), pg.FULLSCREEN)
                if event.key == pg.K_F2:    # F2キーが押されると元に戻る
                    screen = pg.display.set_mode((1920, 1060))
                if event.key == pg.K_SPACE: # スペースキー
                    if jamp == False and chara_live == True:
                        jamp = True
                        y += 1

        # 背景スクロールの描画
        if chara_live:
            x = (tmr%40)*4
            if x == 0:
                count += 1
                if count >= len(syougai):
                    count = 0
        for i in range(17):
            num = count
            hantei = int(i+num)
            if num+16 >= len(syougai):
                hantei = int(i+num)%len(syougai)
            if syougai[hantei] == 1:
                scrn_sfc.blit(img_bg[0], [i*160-x, 0])
            elif syougai[hantei] == 0:
                scrn_sfc.blit(img_bg[1], [i*160-x, 0])
                if i == 1 and x >= 30 and y == 580:
                    chara_live = False
        
        if chara_live:
            if tmr%50 == 0:
                y = jamp_chara()
        else:
            if y < 1920+240:
                y += 10         # キャラクターが（穴によって）死んだ判定になったら穴の底に落ちる
        scrn_sfc.blit(img_chara[(count%4)], [120, y])    # キャラクターの描画

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()