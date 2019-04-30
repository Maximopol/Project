import configparser

import pygame
from pygame import *

from old import Game
from old.Ini import write_ini_file
import os

ICON_DIR = os.path.dirname(__file__)
WIDTH_WINDOW = 1100
HEIGHT_WINDOW = 640
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FON = (int(write_ini_file().get("Game zone", "color1")), int(write_ini_file().get("Game zone", "color2")),
       int(write_ini_file().get("Game zone", "color3")))


def show_skin_menu(screen, bg, flag):
    mousex = mousey = mousexC = mouseyC = 0

    screen.blit(bg, (0, 0))
    pygame.font.init()

    config = configparser.ConfigParser()
    config.read("%s/settings.ini" % ICON_DIR)

    p1 = transform.scale(image.load("%s/image/others/platform.png" % ICON_DIR), (20, 20))
    p2 = transform.scale(image.load("%s/image/others/platform2.png" % ICON_DIR), (20, 20))
    p3 = transform.scale(image.load("%s/image/others/platform3.png" % ICON_DIR), (20, 20))
    p4 = transform.scale(image.load("%s/image/others/platform4.png" % ICON_DIR), (20, 20))
    pl1 = transform.scale(image.load("%s/image/player/0.png" % ICON_DIR), (44, 64))
    b1 = transform.scale(image.load("%s/image/bot/bot0.png" % ICON_DIR), (44, 64))

    p22 = transform.scale(image.load("%s/image/others/1.png" % ICON_DIR), (20, 20))
    p33 = transform.scale(image.load("%s/image/others/2.png" % ICON_DIR), (20, 20))
    p44 = transform.scale(image.load("%s/image/others/3.png" % ICON_DIR), (20, 20))

    font = pygame.font.SysFont('monospace', 40)

    text1 = font.render('Блоки', False, RED)
    text3 = font.render('Персонажи', False, RED)
    text4 = font.render('Робот', False, RED)
    text10 = font.render('Геймплей', False, RED)
    text11 = font.render('Фоны', False, RED)
    while True:
        text5 = font.render('Назад', False, WHITE)
        text20 = font.render('1 игрок и 1 бот', False, WHITE)
        text30 = font.render('2 игроки и 1 бот', False, WHITE)
        text40 = font.render('2 игроки', False, WHITE)

        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("ВЫХОД")
            if e.type == MOUSEBUTTONUP:
                mousex, mousey = e.pos
            if e.type == MOUSEMOTION:
                mousexC, mouseyC = e.pos

        if Rect(130, 100, 20, 20).collidepoint(mousex, mousey):
            config.set("Game zone", "image of block", "s/image/others/platform.png")

        if Rect(130, 140, 20, 20).collidepoint(mousex, mousey):
            config.set("Game zone", "image of block", "s/image/others/platform2.png")

        if Rect(130, 180, 20, 20).collidepoint(mousex, mousey):
            config.set("Game zone", "image of block", "s/image/others/platform3.png")

        if Rect(130, 220, 20, 20).collidepoint(mousex, mousey):
            config.set("Game zone", "image of block", "s/image/others/platform4.png")

        if Rect(650, 375, 450, 50).collidepoint(mousexC, mouseyC):
            text20 = font.render('1 игрок и 1 бот', False, RED)
            if Rect(650, 375, 450, 50).collidepoint(mousex, mousey):
                flag = 0
                config.set("Others", "start_game", "0")

        elif Rect(650, 450, 450, 50).collidepoint(mousexC, mouseyC):
            text30 = font.render('2 игроки и 1 бот', False, RED)
            if Rect(650, 450, 450, 50).collidepoint(mousex, mousey):
                flag = 1
                config.set("Others", "start_game", "1")

        elif Rect(650, 525, 450, 50).collidepoint(mousexC, mouseyC):
            text40 = font.render('2 игроки', False, RED)
            if Rect(650, 525, 450, 50).collidepoint(mousex, mousey):
                flag = 2
                config.set("Others", "start_game", "2")

        if Rect(130, 350, 20, 20).collidepoint(mousex, mousey):
            config.set("Game zone", "color1", str(0))
            config.set("Game zone", "color2", str(50))
            config.set("Game zone", "color3", str(50))

        if Rect(130, 400, 20, 20).collidepoint(mousex, mousey):
            config.set("Game zone", "color1", str(255))
            config.set("Game zone", "color2", str(151))
            config.set("Game zone", "color3", str(151))

        if Rect(130, 450, 20, 20).collidepoint(mousex, mousey):
            config.set("Game zone", "color1", str(172))
            config.set("Game zone", "color2", str(198))
            config.set("Game zone", "color3", str(155))

        if Rect(400, 550, 300, 50).collidepoint(mousexC, mouseyC):
            text5 = font.render('Назад', False, RED)
            if Rect(500, 550, 350, 70).collidepoint(mousex, mousey):
                with open("%s/settings.ini" % ICON_DIR, "w") as config_file:
                    config.write(config_file)
                return flag

        screen.blit(text10, [700, 300])
        screen.blit(text20, [700, 375])
        screen.blit(text30, [700, 450])
        screen.blit(text40, [700, 525])

        screen.blit(p1, (130, 100))
        screen.blit(p2, (130, 140))
        screen.blit(p3, (130, 180))
        screen.blit(p4, (130, 220))

        screen.blit(pl1, (525, 100))

        screen.blit(b1, (875, 100))

        screen.blit(text1, [40, 25])
        screen.blit(text3, [400, 25])
        screen.blit(text4, [800, 25])
        screen.blit(text5, [450, 550])

        screen.blit(text11, [40, 300])
        screen.blit(p22, [130, 350])
        screen.blit(p33, [130, 400])
        screen.blit(p44, [130, 450])
        pygame.display.flip()


def main(screen, bg):
    screen.blit(bg, (0, 0))
    mousex = mousey = mousexC = mouseyC = 0
    pygame.font.init()
    font = pygame.font.SysFont('monospace', 50)

    display.set_caption("Deadly battle")

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("ВЫХОД")
            if e.type == MOUSEMOTION:
                mousex, mousey = e.pos
            if e.type == MOUSEBUTTONUP:
                mousexC, mouseyC = e.pos

        text1 = font.render('СТАРТ', False, WHITE)
        text2 = font.render('НАСТРОЙКИ', False, WHITE)
        text3 = font.render('ВЫХОД', False, WHITE)

        if Rect(380, 250, 350, 70).collidepoint(mousex, mousey):
            text1 = font.render('СТАРТ', False, RED)
            if Rect(380, 250, 350, 70).collidepoint(mousexC, mouseyC):
                return 0

        elif Rect(380, 350, 350, 70).collidepoint(mousex, mousey):
            text2 = font.render('НАСТРОЙКИ', False, RED)
            if Rect(380, 350, 350, 70).collidepoint(mousexC, mouseyC):
                return 1

        elif Rect(380, 450, 350, 70).collidepoint(mousex, mousey):
            text3 = font.render('ВЫХОД', False, RED)
            if Rect(380, 450, 350, 70).collidepoint(mousexC, mouseyC):
                return -1

        screen.blit(text1, [400, 250])
        screen.blit(text2, [400, 350])
        screen.blit(text3, [400, 450])

        pygame.display.flip()


def start():
    pygame.init()
    pygame.display.set_caption("GAME")
    screen = pygame.display.set_mode([WIDTH_WINDOW, HEIGHT_WINDOW])
    bg = pygame.image.load("F:/Project/image/others/image001.png")
    screen.blit(bg, (0, 0))
    flag = int(write_ini_file().get("Others", "start_game"))
    while 1:
        Game.FON = FON
        if main(screen, bg) == 0:
            Game.main(flag)

        if main(screen, bg) == 1:
            flag = show_skin_menu(screen, bg, flag)

        if main(screen, bg) == -1:
            break
    pygame.quit()


if __name__ == "__main__":
    start()
