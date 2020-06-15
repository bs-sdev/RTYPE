import os

import pygame as pg

from python.src.core.test_4.spritesheet import SpriteSheet

pg.init()

#
clock = pg.time.Clock()

# Window in which the game will be displayed in
window = pg.display.set_mode((500, 500))

# Background representing space in window's background
bg = pg.image.load(os.path.join("../sprites", "SpaceBackground1.png"))

# SpriteSheet class loading a gif image containing space ship sprite, coordinates will be used for each sprite
# succession animation
sp_sheet = SpriteSheet(os.path.join("../sprites", "r-typesheet1.gif"))

# Sprite used while spaceship going right
flyRight = [
    sp_sheet.get_image(x=167, y=2, width=32, height=15)
]

# Sprite used while spaceship going left
flyLeft = [
    sp_sheet.get_image(x=167, y=2, width=32, height=15)
]

# Sprites used while spaceship going down
flyDown = [
    sp_sheet.get_image(x=200, y=2, width=32, height=15),  # Down 1 inverse (soit up_1)
    sp_sheet.get_image(x=233, y=2, width=32, height=15)   # Down 2 inverse (soit up_2)
]

# Sprites used while spaceship going up
flyUp = [
    sp_sheet.get_image(x=134, y=2, width=32, height=15),  # Down 1 inverse (soit down_1)
    sp_sheet.get_image(x=101, y=2, width=32, height=15)  # Down 2 inverse (soit down_2)
]

# Sprites used while spaceship going right to show engine flames
propellant = [
    sp_sheet.get_image(x=133, y=18, width=32, height=32),
    sp_sheet.get_image(x=166, y=18, width=32, height=32),
    sp_sheet.get_image(x=199, y=18, width=32, height=32),
    sp_sheet.get_image(x=232, y=18, width=32, height=32)
]

# Sprites used to show spaceship's firing
beam = [
    sp_sheet.get_image(x=248, y=85, width=17, height=12),
    sp_sheet.get_image(x=231, y=85, width=17, height=12),
    sp_sheet.get_image(x=213, y=85, width=17, height=12)
]

# Sprite used when the ship is in stationary mode (no movement)
char = sp_sheet.get_image(x=167, y=2, width=32, height=15)


class Ship:

    def __init__(self, x, y, width, height):
        """
        Ship's constructor

        :param x: ship's x coordinates
        :param y: ship's y coordinates
        :param width: ship's width
        :param height: ship's height
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.fly_count = 0
        self.propellant_count = 3
        self.fire_count = 0

    def draw(self, win):
        """
        Function that draw the sprites on the given window depending of the action typed by the user.

        Depending of the actions defined (left, right, up, down and no action), in the given window will be drawn the
        right
        :param win: Window in which sprites will be drawn with given algorithm and fly_count index (defining sprite to
                    load in related array)
        :return:
        """
        if self.fly_count + 1 >= 3:
            self.fly_count = 0

        # If going left, animate the going left's sprite (which is no animation)
        if self.left:
            win.blit(flyLeft[0], (self.x, self.y))

        # If going right, animate the propellant showing flames of engine
        elif self.right:
            win.blit(propellant[self.propellant_count], (self.x - 32, self.y - 12))
            win.blit(flyRight[0], (self.x, self.y))
            # if self.fly_count < 3:
            #     self.fly_count += 1
            # else:
            #     self.fly_count = 1

            if self.propellant_count > 0:
                self.propellant_count -= 1
            else:
                self.propellant_count = 0

        # If up, animate up's sprites
        elif self.up:
            win.blit(flyUp[self.fly_count], (self.x, self.y))
            # print("Up N° " + str(fly_count))
            if self.fly_count < 1:
                self.fly_count += 1
            else:
                self.fly_count = 1

        # If up, animate down's sprites
        elif self.down:
            win.blit(flyDown[self.fly_count], (self.x, self.y))
            # print("Down N° " + str(fly_count))
            if self.fly_count < 1:
                self.fly_count += 1
            else:
                self.fly_count = 1

        # If no action, load stationary position sprite
        else:
            win.blit(char, (self.x, self.y))


class Projectile:

    def __init__(self, x, y, beam_index):
        """
        Beam's constructor

        :param x: beam's x coordinate
        :param y: beam's y coordinate
        :param beam_index: beam's sprite index to load
        """
        self.x = x
        self.y = y
        # self.radius = radius
        # self.color = color
        self.facing = 1
        self.vel = 8 * self.facing
        self.beam_index = beam_index

    def draw(self, win):
        # pg.draw.circle(win, self.color, (self.x, self.y), self.radius, 1)
        # load du sprite
        # Il faut checker l'index pour supprimer les deux premiers sprite
        win.blit(beam[self.beam_index], (self.x + 16, self.y - 7))


def redraw_game_window(ship):
    """
    Redraw the ship in the window (global variable)

    :param ship: Ship to redraw in window
    :return: display updated
    """

    window.blit(bg, (0, 0))

    ship.draw(win=window)

    for bullet in bullets:
        bullet.draw(window)

    pg.display.update()


########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
#                                                   Main Loop                                                          #
#                                                                                                                      #
########################################################################################################################
run = True
ship = Ship(x=250, y=250, width=32, height=15)
bullets = []

while run:
    clock.tick(30)
    # clock.tick(10)  #  ONLY FOR DEBUG PURPOSE

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE]:
        # if len(bullets) < 5:
        if len(bullets) < 3:
            print("LEN OF BULLETS: " + str(len(bullets)))
            # bullets.append(Projectile(round(ship.x + ship.width // 2), round(ship.y + ship.height // 2), 6, (255, 255, 255), ))
            # Pour insérer les sprite dans le tableau à la place des cercles (radius et color), doivent être remplacer
            # par les sprites de feu (3 sprites au total)
            # bullets.append(Projectile(round(ship.x + ship.width // 2), round(ship.y + ship.height // 2), len(bullets)))
            bullets.append(Projectile(round(ship.x + ship.width // 2), round(ship.y + ship.height // 2), 0))

    if keys[pg.K_LEFT] and ship.x > ship.vel:
        ship.x -= ship.vel
        ship.left = True
        ship.right = False

    elif keys[pg.K_RIGHT] and ship.x < 500 - ship.width - ship.vel:
        ship.x += ship.vel
        ship.right = True
        ship.left = False

    elif keys[pg.K_DOWN] and ship.y < 500 - ship.height - ship.vel:
        ship.y += ship.vel
        ship.up = True
        ship.down = False

    elif keys[pg.K_UP] and ship.y > ship.vel:
        ship.y -= ship.vel
        ship.up = False
        ship.down = True

    else:
        ship.right = False
        ship.left = False
        ship.up = False
        ship.down = False
        ship.fly_count = 0
        ship.propellant_count = 3

    redraw_game_window(ship=ship)

pg.quit()
