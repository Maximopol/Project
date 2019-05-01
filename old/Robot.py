import configparser

import math as m
from pygame import *
import os
from old.Ini import write_ini_file
from old.Player import Player1
from old.Pyganim import PygAnimation

config = configparser.ConfigParser()

ICON_DIR = os.path.dirname(__file__)
config.read("%s/settings.ini" % ICON_DIR)

ANIMATION_RIGHT = ['F:/Project/image/bot/botr11.png', 'F:/Project/image/bot/botr2.png',
                   'F:/Project/image/bot/botr3.png', 'F:/Project/image/bot/botr4.png']
ANIMATION_LEFT = ['F:/Project/image//bot/botl1.png', 'F:/Project/image//bot/botl2.png',
                  'F:/Project/image//bot/botl3.png',
                  'F:/Project/image//bot/botl4.png']
ANIMATION_DELAY = 0.1
ANIMATION_STAY = [('F:/Project/image/bot/bot00.png', 0.1)]
ANIMATION_DEATH = [('F:/Project/image/bot/bot_grave.png', 0.1)]

SPEED = int(config.get("Bot", "speed"))

BLOCK_W = BLOCK_H = 20


class Robot(Player1):
    def __init__(self, x, y, kek):
        self.FON = (int(write_ini_file().get("Game zone", "color1")), int(write_ini_file().get("Game zone", "color2")),
                    int(write_ini_file().get("Game zone", "color3")))
        sprite.Sprite.__init__(self)
        super(Robot, self).__init__(x, y, kek)
        self.save = [x, y]
        self.image = image.load('F:/Project/image/bot/bot_grave.png')
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = PygAnimation(boltAnim)
        self.boltAnimRight.play()
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimDeath = PygAnimation(ANIMATION_DEATH)
        self.boltAnimDeath.play()

    def collide(self, list_block):
        blocks = sprite.spritecollide(self, list_block, False)
        if len(blocks) != 0:
            save_x = self.rect.x
            self.rect.x = self.save[0]
            if len(sprite.spritecollide(self, list_block, False)) == 0:
                pass
            else:
                self.rect.x = save_x
                self.rect.y = self.save[1]
                if len(sprite.spritecollide(self, list_block, False)) == 0:
                    pass
                else:
                    self.rect.x = self.save[0]

    def search_player(self, b1x, b1y, b2x, b2y):
        if (m.fabs(self.rect.x - b1x) + m.fabs(self.rect.y - b1y)) > (
                m.fabs(self.rect.x - b2x) + m.fabs(self.rect.y - b2y)):
            self.__move(b2x, b2y)
        else:
            self.__move(b1x, b1y)

    def __move(self, bx, by):
        self.save[0] = self.rect.x
        self.save[1] = self.rect.y

        if m.fabs(self.rect.y - by) < 11:
            self.attack()

        if self.rect.x > bx:
            self.rect.x -= SPEED
            self.facing = -1
            self.image.fill(self.FON)
            self.boltAnimLeft.blit(self.image, (0, 0))
        else:
            self.rect.x += SPEED
            self.facing = 1
            self.image.fill(self.FON)
            self.boltAnimRight.blit(self.image, (0, 0))

        if self.rect.y > by:
            self.rect.y -= SPEED
        else:
            self.rect.y += SPEED

    def attack(self):
        if self.second < 0:
            self.bullets.append(self.patron(self.rect.x + 11, self.rect.y + 16, (255, 100, 100), self.facing))
            self.second = 12

    def update(self, list_block, b1, b2, pharmacy):

        if self._health > 0:
            self.died(b1.bullet, b2.bullet, b1, b2)
            self.search_player(b1.x, b1.y, b2.x, b2.y)
            self.collide(list_block)
            self.rotate_rect.center = self.rect.center
            self.search_different_blocks(pharmacy)
            self.second -= 1

            for bul in self.bullets:
                if bul.collide(list_block):
                    self.bullets.pop(self.bullets.index(bul))

        else:
            self.image.fill(self.FON)
            self.boltAnimDeath.blit(self.image, (0, 0))

    def update1(self, list_block, b1, pharmacy):

        if self._health > 0:
            self.injury(b1.bullet, b1)
            self.__move(b1.x, b1.y)
            self.collide(list_block)
            self.rotate_rect.center = self.rect.center
            self.search_different_blocks(pharmacy)
            self.second -= 1

            for bul in self.bullets:
                if bul.collide(list_block):
                    self.bullets.pop(self.bullets.index(bul))

        else:
            self.image.fill(self.FON)
            self.boltAnimDeath.blit(self.image, (0, 0))
