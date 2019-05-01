from pygame import draw, Rect, Surface
from old.Ini import write_ini_file
from abc import ABC, abstractmethod

SPEED = int(write_ini_file().get("Others", "speed of bullet"))
RADIUS = int(write_ini_file().get("Others", "radius bullet"))
BLOCK_SIZE = int(write_ini_file().get("Others", "block size"))


class Patron(ABC):
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


class Patron2(Patron):
    DEFAULT_SPEED = 10
    DEFAULT_DAMAGE = 3

    def __init__(self, x, y, color, facing):
        super().__init__(x, y)
        self.radius = RADIUS
        self.color = color
        self.facing = facing
        self.vel = self.DEFAULT_SPEED * facing

    def drawing(self, win: Surface):
        draw.circle(win, self.color, (self.x, self.y), self.radius)
        self.x += self.vel

    def damage(self):
        return self.DEFAULT_DAMAGE


class Patron3(Patron):
    DEFAULT_SPEED = 15

    def __init__(self, x, y, color, facing):
        super().__init__(x, y)

        self.color = color
        self.facing = facing
        self.vel = self.DEFAULT_SPEED * facing

    def drawing(self, win: Surface):
        draw.ellipse(win, self.color, (self.x, self.y, 4, 2))
        self.x += self.vel

    def damage(self):
        return super().DEFAULT_DAMAGE
