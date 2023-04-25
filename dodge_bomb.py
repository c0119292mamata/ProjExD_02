import pygame as pg
import sys
import random
import math

delta = {
    pg.K_UP:(0,-1),
    pg.K_DOWN:(0,1),
    pg.K_LEFT:(-1,0), 
    pg.K_RIGHT:(1,0)
         }


def check_bound(scr_rct:pg.Rect,obj_rct:pg.Rect): 
    """
    オブジェクトが画面内or画面外を判定し　真理値タブルを返す関数
    引数1：画面SurfaceのRect
    引数2：こうかとん、又は、爆弾SurfaceのRect
    戻り値：横方向、縦方向のはみ出し判定結果(画面内：True/画面外：False)
    """
    yoko,tate = True,True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko,tate


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
                """if kk_rct.centerx+r>=1600 and k==pg.K_RIGHT:
                    kk_rct.move_ip(-mv[0],-mv[1])
                if kk_rct.centerx-r<=0 and k==pg.K_LEFT: 
                    kk_rct.move_ip((1,0))
                if kk_rct.centery+r>=900 and k==pg.K_DOWN:
                    kk_rct.move_ip((0,-1))
                if kk_rct.centery-r<=0 and k==pg.K_UP:
                    kk_rct.move_ip((0,1))"""
        
        if check_bound(screen.get_rect(),kk_rct)!=(True,True):
            for k,mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0],-mv[1])
                    
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        
        bb_rct.move_ip(vx,vy)  # 爆弾を動かす
        
        yoko,tate = check_bound(screen.get_rect(),bb_rct)
        if yoko != True:
            vx*=-1
        if tate != True:
            vy*=-1
        """if bb_rct.centerx+10>=1600 or bb_rct.centerx-10<=0:
            vx*=-1
        if bb_rct.centery+10>=900 or bb_rct.centery-10<=0:
            vy*=-1"""
        screen.blit(bb_img, bb_rct)
        
        
        """dist=math.sqrt((bb_rct.centerx-kk_rct.centerx)**2+
              (bb_rct.centery-kk_rct.centery)**2)
        dist_01=math.sqrt((10-50)**2*2)
        if dist<=dist_01:
            return 0"""
        if kk_rct.colliderect(bb_rct):
            return 0
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()