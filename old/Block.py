import os
import random

from pygame import sprite, image, Surface, Rect

from old.Ini import write_ini_file
from old.Pyganim import PygAnimation

ICON_DIR = os.path.dirname(__file__)
WIDTH_WINDOW = int(write_ini_file().get("Game zone", "width window"))
HEIGHT_WINDOW = int(write_ini_file().get("Game zone", "height window"))
BLOCK_SIZE = int(write_ini_file().get("Others", "block size"))

ANIMATION_MONSTER = ['F:/Project/image/others/MONSTR1.png', 'F:/Project/image/others/MONSTR2.png']


class Block(sprite.Sprite):
    """Create blocks for the game.
    'location' is the place where the images of the block are stored """

    def __init__(self, location):
        sprite.Sprite.__init__(self)
        self.image = Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image = image.load(location)
        self.rect = self.image.get_rect()

    @property
    def x(self): return self.rect.x

    @property
    def y(self): return self.rect.y


class Medicines(sprite.Sprite):
    def __init__(self, location):
        sprite.Sprite.__init__(self)
        self.image = image.load(location)
        self.rect = self.image.get_rect()
        self.__replace()
        self.wasTaken = False

    def update(self, list_block):
        self.__collide(list_block)
        self.__check_total()

    def __replace(self):
        self.rect.x = random.randrange(0, WIDTH_WINDOW, BLOCK_SIZE)
        self.rect.y = random.randrange(40, HEIGHT_WINDOW, BLOCK_SIZE)

    def __check_total(self):
        if self.wasTaken:
            self.__replace()
            self.wasTaken = False
        else:
            pass

    def __collide(self, list_block):
        for p in list_block:
            if self.rect.x == p.x and self.rect.y == p.y:
                self.__replace()

    def used(self):
        self.wasTaken = True


class Monster(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image = image.load('F:/Project/image/others/MONSTR1.png')
        self.rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.yvel = self.xvel = 1
        boltAnim = []
        for anim in ANIMATION_MONSTER:
            boltAnim.append((anim, 0.3))
        self.boltAnim = PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self, platforms):

        self.boltAnim.blit(self.image, (0, 0))

        self.rect.y += self.xvel
        self.rect.x += self.yvel

        self.collide(platforms)

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                self.xvel = -self.xvel
                self.yvel = -self.yvel
                self._replace()

    def _replace(self):

        self.rect.x = random.randrange(0, WIDTH_WINDOW, BLOCK_SIZE)
        self.rect.y = random.randrange(40, HEIGHT_WINDOW, BLOCK_SIZE)

    def damage(self):
        self._replace()
        if random.randint(1, 100) == 1:
            return 30
        else:
            return random.randint(1, 5)
