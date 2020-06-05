import pygame as pg


class SpriteSheet:
    # Utility class for loading and parsing sprite sheet

    def __init__(self, filename):
        self.sprite_sheet = pg.image.load(filename).convert()
        # self.sprite_sheet = pg.image.load(filename)

    def get_image(self, x, y, width, height):
        # grab an image from a larger sprite sheet
        image = pg.Surface((width, height), pg.SRCALPHA)  # SRCALPHA allow to remove the black background.
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        return image
