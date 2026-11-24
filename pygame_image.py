import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, [-tmr, 0])  # 背景を毎フレーム左に1ピクセルずらす
        screen.blit(kk_img, [300, 200])  # 背景の上にこうかとんを描く
        pg.display.update()
        tmr += 1
        clock.tick(200)  # 最大200 FPSに制限する


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()