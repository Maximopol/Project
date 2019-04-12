from pygame import Surface, image

from blocks.Govno import Govno


class Block(Govno):
    # def __init__(self):
    #     sprite.Sprite.__init__(self)
    #     self.image = Surface((20, 20))
    #     self.image.fill(Color("#FF6262"))
    #
    #     self.rect = self.image.get_rect()
    """Create blocks for the game.
       'location' is the place where the images of the block are stored """

    def __init__(self, location):
        super().__init__()
        self.image = Surface((20, 20))
        self.image = image.load(location)
        self.rect = self.image.get_rect()
        self._x = None
        self._y = None
