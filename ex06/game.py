import pygame as pg
import sys
import time
import math

# ステージリスト（12の倍数個じゃなくてもなんでも大丈夫です）
# 0:穴, 1:地面, 2:岩
syougai = [
    1, 1, 1, 1, 1, 0, 1, 1 , 1, 1, 1, 1, 2, 1, 1, 1,
    1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1,
    1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0,
    1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0
    ]

jamp = False
jamp_high = 160
jamp_kakeru = 1/5
jamp_count = 0
y = 580


def jamp_chara():  # キャラクターのジャンプ関数
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
    w = 1920
    h = 1060
    scrn_sfc = pg.display.set_mode((w, h))        # 画面サイズ
    scrn_rct = scrn_sfc.get_rect()
    clock = pg.time.Clock()
    # 開始時間(内野)
    s_time = time.time()

    # 背景画像
    img_bg = [
        pg.image.load("ex06/bg.jpg").convert(),
        pg.image.load("ex06/ana.jpg").convert()
    ]
    #img_bg_rct = img_bg.get_rect()
    img_chara = [
        pg.image.load("ex06/human_1.png").convert_alpha(),
        pg.image.load("ex06/human_2.png").convert_alpha(),
        pg.image.load("ex06/human_3.png").convert_alpha(),
        pg.image.load("ex06/human_4.png").convert_alpha()
    ]
    img_iwa = pg.image.load("ex06/iwa.png").convert_alpha()
    img_kumo = pg.image.load("ex06/kumo.png").convert_alpha()
    chara_live = 1   # キャラクターの生存判定
    death_reason = 0    # 1:穴, 2:岩
    tmr = 0
    count = 0

    # GameOver画面の設定(内野)
    fonto = pg.font.Font(None, 200)
    small_fonto = pg.font.Font(None, 100)
    gameover_text = fonto.render(str("Game Over"), True, (255, 0, 0))
    gameover_text_rct = gameover_text.get_rect(
        center=(1920//2, 1080//2))
    gameover_comment = small_fonto.render(
        str("press space to finish"), True, (0, 0, 0))
    gameover_comment_rct = gameover_text.get_rect(
        center=(1920//2, 900))

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
                if event.key == pg.K_SPACE:  # スペースキー
                    if jamp == False and chara_live == True:
                        jamp = True
                        y += 1

        # 背景スクロールの描画
        if chara_live:      # キャラクターが生きていたら
            x = (tmr % 40)*4
            if x == 0:
                count += 1
                if count >= len(syougai):
                    count = 0
        for i in range(17):
            num = count
            hantei = int(i+num)
            if num+16 >= len(syougai):
                hantei = int(i+num) % len(syougai)
            if syougai[hantei] > 0:
                scrn_sfc.blit(img_bg[0], [i*160-x, 0])  # 地面がある背景の描画
                if syougai[hantei] == 2:  # 岩の描画
                    scrn_sfc.blit(img_iwa, [i*160-x, 700])
                    if i == 1 and x >= 30 and y >= 460:
                        chara_live = 0
                        death_reason = 2
            elif syougai[hantei] == 0:
                scrn_sfc.blit(img_bg[1], [i*160-x, 0])  # 地面が無い背景（穴）の描画
                if i == 1 and x >= 30 and y == 580:
                    chara_live = 0
                    death_reason = 1

        # 経過時間の表示(内野)
        if death_reason == 0:
            score_time = time.time() - s_time
        txt = fonto.render(str(math.floor(score_time)), True, (0, 0, 0))
        scrn_sfc.blit(txt, (0, 0))

        if chara_live:
            if tmr % 50 == 0:
                y = jamp_chara()
            scrn_sfc.blit(img_chara[(count % 4)], [120, y])    # キャラクターの描画  
        else:
            if death_reason == 1:
                if y < 1920+240:
                    scrn_sfc.blit(img_bg[1], (130, 0))
                    y += 10         # キャラクターが（穴によって）死んだ判定になったら穴の底に落ちる
                    scrn_sfc.blit(img_chara[(count % 4)], [120, y])    # キャラクターの描画 
                # GameOver機能(内野)
                else:
                    scrn_sfc.blit(gameover_text, gameover_text_rct)

                    scrn_sfc.blit(gameover_comment, gameover_comment_rct)

                    score_text = fonto.render(
                        str(f"SCORE : {math.floor(score_time)}"), True, (0, 0, 0))
                    score_text_rct = score_text.get_rect(
                        center=(1920//2, 700))
                    scrn_sfc.blit(score_text, score_text_rct)

                    key_status = pg.key.get_pressed()

                    if key_status[pg.K_SPACE]:
                        return

            elif death_reason == 2:
                scrn_sfc.blit(img_bg[0], [i*160-x, 0])
                scrn_sfc.blit(img_chara[(count % 4)], [120, y])    # キャラクターの描画
                scrn_sfc.blit(gameover_text, gameover_text_rct)
                scrn_sfc.blit(gameover_comment, gameover_comment_rct)

                score_text = fonto.render(
                    str(f"SCORE : {math.floor(score_time)}"), True, (0, 0, 0))
                score_text_rct = score_text.get_rect(
                    center=(1920//2, 700))
                scrn_sfc.blit(score_text, score_text_rct)

                key_status = pg.key.get_pressed()
                if key_status[pg.K_SPACE]:
                    return
        
        # 雲を表示（吉田）
        scrn_sfc.blit(img_kumo, (200, 100))

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
