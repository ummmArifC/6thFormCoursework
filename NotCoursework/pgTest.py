import pygame as pg

def menuScreen():   #subroutine that is the main game loop 
    pg.init()
    menuScreen = pg.display.set_mode((1280, 700), pg.RESIZABLE)
    clock = pg.time.Clock()
    running = True

    while running == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False     #functions would be called here in the main loop


        menuScreen.fill("black")    

        pg.display.flip()

        clock.tick(60)

    pg.quit()
menuScreen()