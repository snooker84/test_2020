import pygame
import sys

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 400
WHITE = (255, 255, 255)
INDIGO = (75, 0, 130)

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

x = 0
backward_flag = 0
rect_size = 100

while 1:
    if x == WIN_WIDTH - rect_size:
        backward_flag = 1
    if x == 0:
        backward_flag = 0

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # заливаем фон
    sc.fill(WHITE)
    # рисуем квадрат
    pygame.draw.rect(sc, INDIGO, (0 + x, WIN_HEIGHT//2 - rect_size//2, rect_size, rect_size))
    # обновляем окно
    pygame.display.update()
    if backward_flag == 0:
        x += 2
    else:
        x -= 2

    clock.tick(FPS)
