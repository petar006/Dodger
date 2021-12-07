import pygame as pg
import time
pg.init()
pg.display.set_caption('pygame')
(sirina,visina)=(1280,720)
prozor=pg.display.set_mode((sirina,visina))
ix=640
iy=375

def crtanje():
    for i in range(265,1015,30):
        pg.draw.line(prozor,pg.Color("Blue"),(i,60),(i,630))
    for i in range(60,660,30):
        pg.draw.line(prozor,pg.Color("Blue"),(265,i),(985,i))
b1=True
b2=True
b3=True
b4=True
b5=True
b6=True
b7=True
b8=True
b1x=610
b1y=525
b2x=760
b2y=465
b3x=310
b3y=165
b4x=460
b4y=315
b5x=910
b5y=315
b6x=520
b6y=525
b7x=640
b7y=225
b8x=370
b8y=135
pg.draw.circle(prozor,pg.Color("Green"),(b1x,b2x),15,1)
pg.draw.circle(prozor,pg.Color("Green"),(b2x,b2y),15,1)
pg.draw.circle(prozor,pg.Color("Green"),(b3x,b3y),15,1)
pg.draw.circle(prozor,pg.Color("Green"),(b4x,b4y),15,1)
pg.draw.circle(prozor,pg.Color("Green"),(b5x,b5y),15,1)
pg.draw.circle(prozor,pg.Color("Green"),(b6x,b6y),15,1)
pg.draw.circle(prozor,pg.Color("Green"),(b7x,b7y),15,1)
pg.draw.circle(prozor,pg.Color("Green"),(b8x,b8y),15,1)
def bobice():
    if ix==b1x and iy==b1y:
        b1==False
    if ix==b2x and iy==b2y:
        b2==False
    if ix==b3x and iy==b3y:
        b3==False
    if ix==b4x and iy==b4y:
        b4==False
    if ix==b5x and iy==b5y:
        b5==False
    if ix==b6x and iy==b6y:
        b6==False
    if ix==b7x and iy==b7y:
        b7==False
    if ix==b8x and iy==b8y:
        b8==False
    if b1==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b1x,b1y),15,1)
    if b2==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b2x,b2y),15,1)
    if b3==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b3x,b3y),15,1)
    if b4==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b4x,b4y),15,1)
    if b5==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b5x,b5y),15,1)
    if b6==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b6x,b6y),15,1)
    if b7==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b7x,b7y),15,1)
    if b8==True:
        pg.draw.circle(prozor,pg.Color("Green"),(b8x,b8y),15,1)








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
            bobice()
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if keys[pg.K_UP] and iy-30>=75:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            iy=iy-30
            bobice()
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if keys[pg.K_LEFT] and ix-30>=280:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            ix=ix-30
            bobice()
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if keys[pg.K_RIGHT] and ix+30<=970:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            ix=ix+30
            bobice()
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
            bobice()
            nx=nx-30
            pg.draw.circle(prozor,pg.Color("Red"),(nx,ny),15,1)
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if a==False and kretnja==True and pucanj==False:
            pg.time.wait(200)
            prozor.fill(pg.Color("Black"))
            crtanje()
            bobice()
            nx=nx+30
            pg.draw.circle(prozor,pg.Color("Red"),(nx,ny),15,1)
            pg.draw.circle(prozor,pg.Color("Yellow"),(ix,iy),15,1)
        if kretnja==False and pucanj==True:
            pg.time.wait(100)
            prozor.fill(pg.Color("Black"))
            crtanje()
            bobice()
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