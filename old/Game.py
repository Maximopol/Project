from time import sleep

import pygame

from old.Block import Block
from old.Player import *
from old.Robot import Robot

WIDTH_WINDOW = int(write_ini_file().get("Game zone", "width window"))
HEIGHT_WINDOW = int(write_ini_file().get("Game zone", "height window"))
BLOCK_SIZE = int(write_ini_file().get("Others", "block size"))
FON = (int(write_ini_file().get("Game zone", "color1")), int(write_ini_file().get("Game zone", "color2")),
       int(write_ini_file().get("Game zone", "color3")))

level = ['                                                       ',
         '                                                       ',
         '-------------------------------------------------------',
         '-                                                     -',
         '-       *                                             -',
         '-                                                     -',
         '-                     ---------                       -',
         '------                                  --       ------',
         '-                                                     -',
         '-                                           ---       -',
         '-                  ----------    -----------          -',
         '-                   -              -                  -',
         '-                    -            -                   -',
         '------                -          -                    -',
         '-                   ------  -----                     -',
         '-                                                     -',
         '-                                               -------',
         '-                                                     -',
         '-         -                        ---                -',
         '-         -                                           -',
         '-         -                                   -       -',
         '-         -                                           -',
         '-         -----  ----------       ------------      ---',
         '-                                                     -',
         '-   -                                                 -',
         '-                                                     -',
         '-                          -      -                   -',
         '------                    --      --             ------',
         '-                        ---      ---                 -',
         '-         --            ----      ----                -',
         '-         --           -----      -----               -',
         '-------------------------------------------------------', ]

list_block = sprite.Group()
all_list = sprite.Group()
hilka_list = sprite.Group()


def create_map():
    x = y = 0
    for z in level:
        for n in z:
            if n == '-':
                block = Block(str(write_ini_file().get("Game zone", "image of block")))
                block.rect.x = x
                block.rect.y = y
                list_block.add(block)
                all_list.add(block)
            x += BLOCK_SIZE
        x = 0
        y += BLOCK_SIZE


def winner(b1, b2, b3):
    if b1 <= 0 and b2 <= 0:
        return "ВЫЙГРАЛ БОТ!"
    elif b2 <= 0 and b3 <= 0:
        return "ВЫЙГРАЛ 1ЫЙ ИГРОК!"
    elif b3 <= 0 and b1 <= 0:
        return "ВЫЙГРАЛ 2ЫЙ ИГРОК!"
    else:
        return "никто"


def draw(bullets, screen):
    for bullet in bullets:
        bullet.draw(screen)


def window1(body1, body2, bot):
    flag = True
    display.init()
    screen = display.set_mode([WIDTH_WINDOW, HEIGHT_WINDOW])
    bg = Surface((WIDTH_WINDOW, HEIGHT_WINDOW))
    font.init()

    bg.fill((int(write_ini_file().get("Game zone", "color1")), int(write_ini_file().get("Game zone", "color2")),
             int(write_ini_file().get("Game zone", "color3"))))
    myfont = pygame.font.SysFont("monospace", 30)
    win = pygame.font.SysFont("monospace", 40)

    apte4ka1 = Medicines("F:/Project/image/others/Medicines.png")
    apte4ka2 = Medicines("F:/Project/image/others/Medicines.png")
    hilka_list.add(apte4ka1)

    mnt = Monster(600, 200)
    hilka_list.add(mnt)
    all_list.add(mnt)
    mn = Monster(190, 200)
    hilka_list.add(mn)
    all_list.add(mn)
    all_list.add(apte4ka1)
    hilka_list.add(apte4ka2)
    all_list.add(apte4ka2)

    while flag:
        for e in event.get():
            if e.type == QUIT:
                raise SystemExit("ВЫХОД")
        screen.blit(bg, (0, 0))
        label = myfont.render("Hp 1ого игрока:" + str(body1.health) + "   Hp 2ого игрока:" + str(body2.health) +
                              "   Hp бота:" + str(bot.health), 1, (255, 255, 0))
        screen.blit(label, (0, 0))
        body1.update(list_block, body2, bot, hilka_list)
        body2.update(list_block, body1, bot, hilka_list)
        bot.update(list_block, body1, body2, hilka_list)
        for f in hilka_list:
            f.update(list_block)

        draw(bot.bullet, screen)
        draw(body1.bullet, screen)
        draw(body2.bullet, screen)

        for f in hilka_list:
            screen.blit(f.image, f.rect)
        screen.blit(body1.image, body1.rotate_rect)
        screen.blit(body2.image, body2.rotate_rect)
        screen.blit(bot.image, bot.rotate_rect)
        list_block.draw(screen)
        if not (winner(body1.health, body2.health, bot.health) == "никто"):
            screen.blit(bg, (0, 0))
            lal = win.render(winner(body1.health, body2.health, bot.health), 1, (255, 255, 0))
            screen.blit(lal, (400, 200))
            flag = False
        display.update()
    sleep(3)
    bg.fill((0, 50, 50))
    screen.blit(bg, (0, 0))


def window2(body1, bot, corrected):
    if corrected:
        mes = "   Hp 2ого игрока:"
        win_mes = "ВЫЙГРАЛ 2ЫЙ ИГРОК!"
    else:
        mes = "   Hp бота:"

    flag = True
    display.init()
    screen = display.set_mode([WIDTH_WINDOW, HEIGHT_WINDOW])
    bg = Surface((WIDTH_WINDOW, HEIGHT_WINDOW))
    font.init()

    # bg.fill((0, 50, 50))
    bg.fill((int(write_ini_file().get("Game zone", "color1")), int(write_ini_file().get("Game zone", "color2")),
             int(write_ini_file().get("Game zone", "color3"))))
    myfont = pygame.font.SysFont("monospace", 30)
    win = pygame.font.SysFont("monospace", 40)

    apte4ka1 = Medicines("%s/image/others/Medicines.png" % ICON_DIR)
    hilka_list.add(apte4ka1)
    all_list.add(apte4ka1)

    mn = Monster(190, 200)
    hilka_list.add(mn)
    all_list.add(mn)
    mnt = Monster(600, 200)
    hilka_list.add(mnt)
    all_list.add(mnt)

    while flag:
        for e in event.get():
            if e.type == QUIT:
                raise SystemExit("ВЫХОД")
        screen.blit(bg, (0, 0))
        label = myfont.render("Hp 1ого игрока:" + str(body1.health) + mes + str(bot.health), 1, (255, 255, 0))
        screen.blit(label, (0, 0))
        body1.update1(list_block, bot, hilka_list)
        bot.update1(list_block, body1, hilka_list)

        for f in hilka_list:
            f.update(list_block)
            screen.blit(f.image, f.rect)

        draw(bot.bullet, screen)
        draw(body1.bullet, screen)

        screen.blit(body1.image, body1.rotate_rect)
        screen.blit(bot.image, bot.rotate_rect)
        list_block.draw(screen)
        if not winner(body1.health, 0, bot.health) == "никто":
            screen.blit(bg, (0, 0))
            if winner(body1.health, 0, bot.health) == "ВЫЙГРАЛ БОТ!" and corrected:
                lal = win.render(win_mes, 1, (255, 255, 0))
            else:

                lal = win.render(winner(body1.health, 0, bot.health), 1, (255, 255, 0))
            screen.blit(lal, (400, 200))
            flag = False
        display.update()
    sleep(3)
    bg.fill((0, 50, 50))
    screen.blit(bg, (0, 0))


def main(flag):
    create_map()
    body1 = Player1(945, 585)
    all_list.add(body1)

    if flag == 1:
        bot = Robot(400, 300)
        body2 = Player2(30, 585)
        all_list.add(body2)
        all_list.add(bot)
        window1(body1, body2, bot)

    elif flag == 2:
        body2 = Player2(30, 585)
        all_list.add(body2)
        window2(body1, body2, True)

    elif flag == 0:
        bot = Robot(400, 300)
        all_list.add(bot)
        window2(body1, bot, False)

    all_list.empty()
    list_block.empty()
    hilka_list.empty()


if __name__ == "__main__":
    main(0)
