from pygame import sprite, Surface, Color


class SimpleBlock(sprite.Sprite):
    """Create blocks for the game.
       'location' is the place where the images of the block are stored """

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.image.fill(Color("#FF6262"))

        self.rect = self.image.get_rect()

    """Returns the X and Y coordinates"""

    @property
    def x(self): return self.rect.x

    @property
    def y(self): return self.rect.y

    @x.setter
    def x(self, value):
        self.rect.x = value

    @y.setter
    def y(self, value):
        self.rect.y = value
