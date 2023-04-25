import pygame as pg
import sys
import random


delta = {
    pg.K_UP:(0,-1),
    pg.K_DOWN:(0,1),
    pg.K_LEFT:(-1,0), 
    pg.K_RIGHT:(1,0)
         }


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)  # 練習1
    bb_img.set_colorkey((0,0,0))  #四隅を透明に
    x=random.randint(10,1590)
    y=random.randint(10,890)
    #screen.blit(bb_img, [x,y])
    vx=+1 ; vy=+1  # 速度の設定
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y
    
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900,400
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
        tmr += 1
        
        r=50
        key_lst = pg.key.get_pressed()
        for k,mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
                if kk_rct.centerx+r>=1600 and k==pg.K_RIGHT:
                    kk_rct.move_ip((-1,0))
                if kk_rct.centerx-r<=0 and k==pg.K_LEFT: 
                    kk_rct.move_ip((1,0))
                if kk_rct.centery+r>=900 and k==pg.K_DOWN:
                    kk_rct.move_ip((0,-1))
                if kk_rct.centery-r<=0 and k==pg.K_UP:
                    kk_rct.move_ip((0,1))
                    
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)  # 爆弾を動かす
        if bb_rct.centerx+10>=1600 or bb_rct.centerx-10<=0:
            vx*=-1
        if bb_rct.centery+10>=900 or bb_rct.centery-10<=0:
            vy*=-1
        screen.blit(bb_img, bb_rct)
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()