from pygame import sprite, Surface, image


class Block(sprite.Sprite):
    # def __init__(self):
    #     sprite.Sprite.__init__(self)
    #     self.image = Surface((20, 20))
    #     self.image.fill(Color("#FF6262"))
    #
    #     self.rect = self.image.get_rect()
    """Create blocks for the game.
       'location' is the place where the images of the block are stored """

    def __init__(self, location):
        sprite.Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.image = image.load(location)
        self.rect = self.image.get_rect()

    """Returns the X and Y coordinates"""

    @property
    def x(self): return self.rect.x

    @property
    def y(self): return self.rect.y
