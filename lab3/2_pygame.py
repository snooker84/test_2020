import pygame as pg
import sys


RESOLUTION = (700, 600)
DELAY = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
FIRE_BRICK = (178, 34, 34)
LIME = (0, 255, 0)
TURQUOISE = (64, 224, 208)
# Отображение поверхности
sc = pg.display.set_mode(RESOLUTION)
# здесь будут рисоваться фигуры
'''r1 = pg.Rect((20, 20, 100, 75))
r2 = pg.Rect((150, 20, 100, 75))
pg.draw.rect(sc, GREEN, r1)
pg.draw.rect(sc, LIGHT_BLUE, r2, 8)
pg.draw.line(sc, FIRE_BRICK, (150, 20), (100, 20), 3)
pg.draw.line(sc, YELLOW, (100, 75), (150, 75), 3)
pg.draw.aaline(sc, PINK, (0, 0), (300, 200))
pg.draw.lines(sc, GREEN, False, [[0, 0], [100, 100], [100, 200], [300, 300]], 2)
pg.draw.aalines(sc, WHITE, True, [[0, 0], [110, 110], [110, 210], [310, 310]], 2)'''
pg.draw.polygon(sc, FIRE_BRICK, [[100, 100], [200, 100], [220, 120], [220, 220], [200, 240], [100, 240], [80, 220],
                                 [80, 120], [100, 100]])
pg.draw.aalines(sc, WHITE, False, [[100, 100], [200, 100], [220, 120], [220, 220], [200, 240], [100, 240], [80, 220],
                                 [80, 120], [100, 100]], 2)
pg.draw.circle(sc, TURQUOISE, (150, 170), 70)
pg.draw.circle(sc, LIME, (150, 170), 95, 3)
pg.draw.ellipse(sc, GREEN, (10, 300, 480, 100))
pi = 3.14
pg.draw.arc(sc, WHITE, (10, 50, 280, 100), 0, pi)
pg.draw.arc(sc, PINK, (50, 30, 200, 150), pi, 2*pi, 3)
# Обновление модуля display
pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(DELAY)
