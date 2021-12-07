import pygame as pg
import time
pg.init()
pg.display.set_caption('pygame')
(sirina,visina)=(1280,720)
prozor=pg.display.set_mode((sirina,visina))

def crtanje():
    for i in range(265,1015,30):
        pg.draw.line(prozor,pg.Color("Blue"),(i,60),(i,630))
    for i in range(60,660,30):
        pg.draw.line(prozor,pg.Color("Blue"),(265,i),(985,i))






def main():
    my=60
    kretnja=True
    pucanj=False
    crtanje()
    ix=640
    iy=375
    nx=280
    ny=45
    pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
    pg.draw.circle(prozor,pg.Color("Red"),(nx,ny),15,1)
    while True:
        prozor.blit
        keys=pg.key.get_pressed()
        if keys[pg.K_DOWN] and iy+30<=615:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            iy=iy+30
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if keys[pg.K_UP] and iy-30>=75:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            iy=iy-30
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if keys[pg.K_LEFT] and ix-30>=280:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            ix=ix-30
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if keys[pg.K_RIGHT] and ix+30<=970:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            ix=ix+30
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if nx+15==985:
            a=True
        if nx-15==265:
            a=False
        if nx==ix:
            kretnja=False
            pucanj=True

        if a==True and kretnja==True and pucanj==False:
            pg.time.wait(200)
            prozor.fill(pg.Color("Black"))
            crtanje()
            nx=nx-30
            pg.draw.circle(prozor,pg.Color("Red"),(nx,ny),15,1)
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if a==False and kretnja==True and pucanj==False:
            pg.time.wait(200)
            prozor.fill(pg.Color("Black"))
            crtanje()
            nx=nx+30
            pg.draw.circle(prozor,pg.Color("Red"),(nx,ny),15,1)
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if kretnja==False and pucanj==True:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            mx=nx
            my=my+30
            pg.draw.circle(prozor,pg.Color("Red"),(nx,ny),15,1)
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
            pg.draw.line(prozor,pg.Color("Red"),(mx,my),(mx,my+30))
            if my>=720:
                kretnja=True
                pucanj=False
                my=60
            if my+15==iy and mx==ix:
                pg.quit()
            

            

        
        
        

        
        pg.display.update()
        for event in pg.event.get(): 
            if event.type==pg.QUIT: 
                pg.quit()

main()