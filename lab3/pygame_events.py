import pygame
import sys

FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
KHAKI = (240, 230, 140)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYUP or i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                y -= 10
            elif i.key == pygame.K_DOWN:
                y += 10
            elif i.key == pygame.K_RIGHT:
                x += 10
            elif i.key == pygame.K_LEFT:
                x -= 10

    sc.fill(WHITE)
    pygame.draw.circle(sc, KHAKI, (x, y), r)
    pygame.display.update()
    clock.tick(FPS)