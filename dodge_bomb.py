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

iro=[(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255,),(255,255,255),(0,0,1)]

def main():
    pg.display.set_caption("逃げろ！こうかとん！頑張れ！")
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
    vx=[1,1,1,1,1,1,1,1] ; vy=[1,1,1,1,1,1,1,1]  # 速度の設定
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y
    bb_imgs=[]
    bb_rcts=[]
    m=[]
    for i in range(8):
        x=random.randint(10,1590)
        y=random.randint(10,890)
        bb_img = pg.Surface((20,20))
        pg.draw.circle(bb_img,iro[i],(10,10),10)
        bb_img.set_colorkey((0,0,0))
        bb_rct = bb_img.get_rect()
        bb_rct.center = x, y
        bb_imgs.append(bb_img)
        bb_rcts.append(bb_rct)
    
    l=1
    kk_rct=kk_img.get_rect()
    kk_rct.center=900,400
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
                
        
        if check_bound(screen.get_rect(),kk_rct)!=(True,True):
            for k,mv in delta.items():
                if key_lst[k]:
                    #direction(mv)
                    kk_rct.move_ip(-mv[0],-mv[1])
                    
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        if tmr%1000==0:
                l+=1
                if l>8:
                    l=8
        for i in range(l):
            bb_rcts[i].move_ip(int(vx[i]),int(vy[i]))  # 爆弾を動かす
            yoko,tate = check_bound(screen.get_rect(),bb_rcts[i])
            if not yoko:
                vx[i]*=-1
            if not tate:
                vy[i]*=-1
            
            screen.blit(bb_imgs[i], bb_rcts[i])
            for j in range(l):
                if i==j:
                    continue
                if bb_rcts[i].colliderect(bb_rcts[j]):
                    vx[i]*=-1
                    vy[i]*=-1
            if kk_rct.colliderect(bb_rcts[i]):
                return 0
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()