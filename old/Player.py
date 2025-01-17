from pygame import *

from old.Block import Medicines, Monster
from old.Ini import write_ini_file
from old.Pyganim import PygAnimation
from guns.bullets.Snarad import Patron3, Patron2
from old.Start import FON
import os

RIGHT_MOVE = int(write_ini_file().get("Players", "speed"))
LEFT_MOVE = -RIGHT_MOVE
JUMP = int(write_ini_file().get("Players", "Jump"))
GRAVITY = float(write_ini_file().get("Others", "gravity"))
ANIMATION_DELAY = 0.1

ICON_DIR = os.path.dirname(__file__)

ANIMATION_RIGHT = ['F:/Project/image/player/r1.png', 'F:/Project/image/player/r2.png',
                   'F:/Project/image/player/r3.png', 'F:/Project/image/player/r4.png',
                   'F:/Project/image/player/r5.png']
ANIMATION_LEFT = ['F:/Project/image/player/l1.png ', 'F:/Project/image/player/l2.png',
                  'F:/Project/image/player/l3.png', 'F:/Project/image/player/l4.png',
                  'F:/Project/image/player/l5.png']
ANIMATION_JUMP_LEFT = [('F:/Project/image/player/jl.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('F:/Project/image/player/jr.png', 0.1)]
ANIMATION_JUMP = [('F:/Project/image/player/j.png', 0.1)]
ANIMATION_STAY = [('F:/Project/image/player/0.png', 0.1)]
ANIMATION_DEATH = [('F:/Project/image/player/died.png', 0.1)]


class Player1(sprite.Sprite):
    def __init__(self, x, y, Patron):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("F:/Project/image/player/0.png"), (22, 32))
        self.image.set_colorkey(FON)
        self._health = 30
        self.rect = self.image.get_rect().move(x, y)
        self.rotate_rect = self.image.get_rect()

        self.patron = Patron

        self.onGround = True
        self.yve = 0
        self.xve = 0
        self.up = self.left = self.right = False
        self.facing = 1
        self.bullets = []
        self.second = 12

        bolt_anim = []
        for anim in ANIMATION_RIGHT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = PygAnimation(bolt_anim)
        self.boltAnimRight.play()
        bolt_anim = []
        for anim in ANIMATION_LEFT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = PygAnimation(bolt_anim)
        self.boltAnimLeft.play()
        self.boltAnimStay = PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))
        self.boltAnimJumpLeft = PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()
        self.boltAnimJumpRight = PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
        self.boltAnimJump = PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

        self.boltAnimDeath = PygAnimation(ANIMATION_DEATH)
        self.boltAnimDeath.play()

    def collide(self, x, y, list_block):
        for p in list_block:
            if sprite.collide_rect(self, p):
                if x > 0:
                    self.rect.right = p.rect.left

                if x < 0:
                    self.rect.left = p.rect.right

                if y > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yve = 0

                if y < 0:
                    self.rect.top = p.rect.bottom
                    self.yve = 0

    def click_button(self):
        if key.get_pressed()[K_RIGHT]:
            self.facing = 1
            self.right = True
            self.left = False

        if key.get_pressed()[K_LEFT]:
            self.facing = -1
            self.left = True
            self.right = False

        if key.get_pressed()[K_UP]:
            self.up = True

        if key.get_pressed()[K_RCTRL]:
            self.attack()

    def move(self, platform):
        self.click_button()

        if self.up:
            if self.onGround:
                self.yve = JUMP
            self.image.fill(FON)
            self.boltAnimJump.blit(self.image, (0, 0))

        if self.left:
            self.xve = LEFT_MOVE
            self.image.fill(FON)
            if self.up:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if self.right:
            self.xve = RIGHT_MOVE
            self.image.fill(FON)
            if self.up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (self.left or self.right):
            self.xve = 0
            if not self.up:
                self.image.fill(FON)
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yve += GRAVITY

        self.onGround = False
        self.rect.y += self.yve
        self.collide(0, self.yve, platform)
        self.rect.x += self.xve
        self.collide(self.xve, 0, platform)
        self.up = self.left = self.right = False
        self.second -= 1

    def attack(self):
        if self.second < 0:
            self.bullets.append(self.patron(self.rect.x + 11, self.rect.y + 16, (100, 100, 150), self.facing))
            self.second = 12

    def update(self, list_block, bob, bot, pharmacy):
        if self._health > 0:
            self.died(bob.bullet, bot.bullet, bob, bot)
            self.move(list_block)
            self.rotate_rect.center = self.rect.center
            self.search_different_blocks(pharmacy)
            for bul in self.bullets:
                if bul.collide(list_block):
                    self.bullets.pop(self.bullets.index(bul))
        else:
            self.rect.x = 1200
            self.rect.y = 1200
            self.image = image.load('F:/Project/image/player/died.png')

    def update1(self, list_block, bot, pharmacy):
        if self._health > 0:
            self.injury(bot.bullet, bot)
            self.move(list_block)
            self.rotate_rect.center = self.rect.center
            self.search_different_blocks(pharmacy)
            for bul in self.bullets:
                if bul.collide(list_block):
                    self.bullets.pop(self.bullets.index(bul))
        else:
            self.rect.x = 1200
            self.rect.y = 1200
            self.image = image.load('F:/Project/image/player/died.png')

    def died(self, bob, bot, b1, b2):
        self.injury(bob, b1)
        self.injury(bot, b2)

    def pop(self, bul):
        self.bullets.pop(self.bullets.index(bul))

    def search_different_blocks(self, blocks):
        for p in blocks:
            if sprite.collide_rect(self, p) and isinstance(p, Medicines):
                self._heal_up()
                p.used()
            if sprite.collide_rect(self, p) and isinstance(p, Monster):
                self._health -= p.damage()

    def _heal_up(self):
        if self._health <= 15:
            self._health += 2

    def injury(self, bob, n):
        for b in bob:
            if Rect(self.rect.x, self.rect.y, 22, 32).collidepoint(b.x, b.y):
                self._health -= b.damage()
                n.pop(b)

    @property
    def bullet(self):
        return self.bullets

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def health(self):
        return self._health


class Player2(Player1):
    def __init__(self, x, y, kek):
        sprite.Sprite.__init__(self)
        super(Player2, self).__init__(x, y, kek)

    def click_button(self):
        if key.get_pressed()[K_d]:
            self.facing = 1
            self.right = True
            self.left = False
        if key.get_pressed()[K_a]:
            self.facing = -1
            self.left = True
            self.right = False
        if key.get_pressed()[K_w]:
            self.up = True
        if key.get_pressed()[K_LSHIFT]:
            self.attack()
