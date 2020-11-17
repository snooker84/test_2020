import pygame as pg
import sys

WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
RED = (255, 0, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

pg.init()
sc = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sc.fill(WHITE)
pg.display.update()
x_pos = 0
y_pos = 0
button_pressed = False
y = SCREEN_HEIGHT
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    if i.type == pg.MOUSEBUTTONDOWN:
        if i.button == 1 and button_pressed == False:
            x_pos = i.pos[0]
            y_pos = i.pos[1]
            button_pressed = True
    if button_pressed:
        sc.fill(WHITE)
        if y_pos <= y:
            pg.draw.circle(sc, BLUE, (x_pos, y), 5)
            y -= 5
        else:
            y = SCREEN_HEIGHT
            pg.draw.rect(sc, RED, (x_pos, y_pos, 10, 10))
            pg.display.update()
            button_pressed = False
    pg.display.update()
    pg.time.delay(20)
