from pygame import draw, Rect
from old.Ini import write_ini_file

SPEED = int(write_ini_file().get("Others", "speed of bullet"))
RADIUS = int(write_ini_file().get("Others", "radius bullet"))
BLOCK_SIZE = int(write_ini_file().get("Others", "block size"))


class Patron(object):
    def __init__(self, x, y, color, facing):
        self.x = x
        self.y = y
        self.radius = RADIUS
        self.color = color
        self.facing = facing
        self.vel = SPEED * facing

    def draw(self, win):
        # draw.ellipse(win, self.color, (self.x, self.y))

        draw.ellipse(win, self.color, (self.x, self.y,2,3))
        # draw.circle(win, self.color, (self.x, self.y), self.radius)
        self.x += self.vel

    def collide(self, blocks):
        for block in blocks:
            if Rect(block.x, block.y, BLOCK_SIZE, BLOCK_SIZE).collidepoint(self.x, self.y):
                return True
        return False
