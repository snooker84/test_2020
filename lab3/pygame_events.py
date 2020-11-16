import pygame
import sys

FPS = 60
W = 700  # ширина экрана
H = 700  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
ORANGE_RED = (255, 69, 0)
RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
DOWN = "to the down"
STOP = "stop"
STOP_L = "stop after left"
STOP_R = "stop after right"
STOP_U = "stop after up"
STOP_D = "stop after down"

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга или прямоугольника
x = W // 2
y = H // 2
r = 20
x_start = x
y_start = y
rect_height = 50
rect_width = 50
motion = STOP

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x_start = x
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                x_start = x
                motion = RIGHT
            if i.key == pygame.K_UP:
                y_start = y
                motion = UP
            elif i.key == pygame.K_DOWN:
                y_start = y
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT]:
                motion = STOP_L
            if i.key in [pygame.K_RIGHT]:
                motion = STOP_R
            if i.key in [pygame.K_UP]:
                motion = STOP_U
            if i.key in [pygame.K_DOWN]:
                motion = STOP_D

    sc.fill(WHITE)
    pygame.draw.rect(sc, ORANGE_RED, (x, y, rect_width, rect_height))
    pygame.display.update()

    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
    elif motion == UP:
        y -= 3
    elif motion == DOWN:
        y += 3
    elif motion == STOP_L and x != x_start:
        x += 3
    elif motion == STOP_R and x != x_start:
        x -= 3
    elif motion == STOP_U and y != y_start:
        y += 3
    elif motion == STOP_D and y != y_start:
        y -= 3

    clock.tick(FPS)
