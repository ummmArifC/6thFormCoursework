import pygame as pg
from buttons import Button  
pg.init()


def mainmenu():
 pg.imiy()
menuScreen = pg.display.set_mode((1280,720), pg.RESIZABLE)
pg.display.set_caption('menu')

#bg = pg.image.load('assets/background.png')
clock = pg.time.Clock()
running = True

while running == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    menuScreen.fill('black')
    pg.display.flip()
    clock.tick(60)

pg.quit()
menuScreen()    




