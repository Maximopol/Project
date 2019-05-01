from abc import ABC, abstractmethod
from pygame import Rect, Surface
from old.Ini import write_ini_file

BLOCK_SIZE = int(write_ini_file().get("Others", "block size"))


class APatron(ABC):
    DEFAULT_DAMAGE = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def drawing(self, win: Surface):
        pass

        # draw.ellipse(win, self.color, (self.x, self.y))

        # draw.ellipse(win, self.color, (self.x, self.y,2,3))
        # # draw.circle(win, self.color, (self.x, self.y), self.radius)
        # self.x += self.vel

    @abstractmethod
    def damage(self):
        pass

    def collide(self, blocks):
        for block in blocks:
            if Rect(block.x, block.y, BLOCK_SIZE, BLOCK_SIZE).collidepoint(self.x, self.y):
                return True
        return False
