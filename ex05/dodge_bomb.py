import pygame as pg
import sys
import random
import time


### Screenクラス
class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title)               # "逃げろ！こうかとん"
        self.sfc = pg.display.set_mode(wh)          # (1600/2, 900/2)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)      # "fig/pg_bg.png"
        self.bgi_sfc = pg.transform.rotozoom(self.bgi_sfc, 0, 0.5)      # 背景画像を0.5倍の大きさにする
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


### Birdクラス
class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)                      # "fig/3.png"
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)    # こうかとんの拡大縮小
        self.rct = self.sfc.get_rect()
        self.rct.center = xy                                    # w/2, h/2
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


### Bombクラス
class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        #self.vx = vxy[0]
        #self.vy = vxy[1]
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Timer:
    def __init__(self, font2, last_game_ended=0):
        self.last_game_ended = last_game_ended
        self.timer = int(pg.time.get_ticks()/1000) - self.last_game_ended
        self.text = font2.render(str(self.timer), True, "red")
        self.rct = self.text.get_rect(center=(40, 30))
    
    def blit(self, scr:Screen):
        self.timer = int(pg.time.get_ticks()/1000) - Timer.last_game_ended
        scr.blit(self.text, self.text_rect)    # タイマーのテキスト
    
    def update(self, last_game_ended, scr:Screen):
        self.last_game_ended = last_game_ended
        self.timer = int(pg.time.get_ticks()/1000) - Timer.last_game_ended
        scr.blit(self.text, self.text_rect)    # タイマーのテキスト


### チェック関数
def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


### メイン関数
def main():
    clock = pg.time.Clock()

    # 練習１
    (w, h) = (int(1600/2), int(900/2))                              # ウィンドウサイズ
    scr = Screen("逃げろ！こうかとん", (w ,h), "fig/pg_bg.jpg")       # Screenクラス

    # 練習３
    (cx, cy) = (w/2, h/2)   # キャラクターの座標
    kkt = Bird("fig/6.png", 1.0, (cx, cy))
    # scrn_sfcにtori_rctに従ってtori_sfcを貼り付ける
    kkt.blit(scr)

    # 練習５（爆弾の作成）
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    bkd.update(scr)

    # フォント
    font2 = pg.font.Font(None, 60)


    while True:
        scr.blit()      # scrn_sfc.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # こうかとんと爆弾のアップデート
        kkt.update(scr)
        bkd.update(scr)

        # こうかとんと爆弾の衝突判定
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()  # main関数の呼び出し
    pg.quit()
    sys.exit()



