from pygame import sprite, Surface, Color


class Govno(sprite.Sprite):
    """Create blocks for the game.
       'location' is the place where the images of the block are stored """

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.image.fill(Color("#FF6262"))

        self.rect = self.image.get_rect()
        self._x = None
        self._y = None

    """Returns the X and Y coordinates"""

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value
