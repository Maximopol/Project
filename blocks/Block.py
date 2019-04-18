from pygame import Surface, image, sprite


class Block(sprite.Sprite):
    """Create blocks for the game.
    'location' is the place where the images of the block are stored """

    def __init__(self, location):
        sprite.Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.image = image.load(location)
        self.rect = self.image.get_rect()
        self._x = None
        self._y = None

    @property
    def x(self): return self.rect.x

    @property
    def y(self): return self.rect.y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value
