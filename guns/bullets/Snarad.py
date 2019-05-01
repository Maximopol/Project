from pygame import draw, Rect, Surface

from guns.ASnarad import APatron
from old.Ini import write_ini_file

SPEED = int(write_ini_file().get("Others", "speed of bullet"))
RADIUS = int(write_ini_file().get("Others", "radius bullet"))
BLOCK_SIZE = int(write_ini_file().get("Others", "block size"))


class Patron2(APatron):
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


class Patron3(APatron):
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


class Patron4(APatron):
    def __init__(self, x, y, color, facing):
        super().__init__(x, y)

    def drawing(self, win: Surface):
        pass

    def damage(self):
        return 0
