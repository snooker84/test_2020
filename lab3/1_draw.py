import pygame as pg


def main():
    pg.display.set_mode((600, 400))
    pg.init()
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return


if __name__ == "__main__":
    main()
