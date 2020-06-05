import os

import pygame as pg

from python.src.core.test_3.spritesheet import SpriteSheet

pg.init()

clock = pg.time.Clock()

window = pg.display.set_mode((500, 500))
bg = pg.image.load(os.path.join("../sprites", "SpaceBackground1.png"))

sp_sheet = SpriteSheet(os.path.join("../sprites", "r-typesheet1.gif"))

flyRight = [
    sp_sheet.get_image(x=167, y=2, width=32, height=15)
]

flyLeft = [
    sp_sheet.get_image(x=167, y=2, width=32, height=15)
]

flyDown = [
    sp_sheet.get_image(x=200, y=2, width=32, height=15),  # Down 1 inverse (soit up_1)
    sp_sheet.get_image(x=233, y=2, width=32, height=15)   # Down 2 inverse (soit up_2)
]

flyUp = [
    sp_sheet.get_image(x=134, y=2, width=32, height=15),  # Down 1 inverse (soit down_1)
    sp_sheet.get_image(x=101, y=2, width=32, height=15)  # Down 2 inverse (soit down_2)
]

char = sp_sheet.get_image(x=167, y=2, width=32, height=15)

propellant = [
    sp_sheet.get_image(x=133, y=18, width=32, height=32),
    sp_sheet.get_image(x=166, y=18, width=32, height=32),
    sp_sheet.get_image(x=199, y=18, width=32, height=32),
    sp_sheet.get_image(x=232, y=18, width=32, height=32)
]

beam = [
    sp_sheet.get_image(x=213, y=85, width=17, height=12),
    sp_sheet.get_image(x=231, y=85, width=17, height=12),
    sp_sheet.get_image(x=248, y=85, width=17, height=12),
    sp_sheet.get_image(x=195, y=85, width=17, height=12)
]

# x = 250
# y = 250
# width = 32
# height = 15
# vel = 5
# is_jump = False
# jump_count = 10
# left = False
# right = False
# up = False
# down = False
# fire = False
# fly_count = 0
# propellant_count = 3
# fire_count = 0


class Ship:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.fly_count = 0
        self.propellant_count = 3
        self.fire_count = 0

    def draw(self, win):
        if self.fly_count + 1 >= 3:
            self.fly_count = 0

        if self.left:
            win.blit(flyLeft[0], (self.x, self.y))

        elif ship.right:
            win.blit(propellant[self.propellant_count], (self.x - 32, self.y - 12))
            win.blit(flyRight[0], (self.x, self.y))
            if self.fly_count < 3:
                self.fly_count += 1
            else:
                self.fly_count = 1

            if self.propellant_count > 0:
                self.propellant_count -= 1
            else:
                self.propellant_count = 0

        elif self.up:
            win.blit(flyUp[self.fly_count], (self.x, self.y))
            # print("Up N° " + str(fly_count))
            if self.fly_count < 1:
                self.fly_count += 1
            else:
                self.fly_count = 1

        elif self.down:
            win.blit(flyDown[self.fly_count], (self.x, self.y))
            # print("Down N° " + str(fly_count))
            if self.fly_count < 1:
                self.fly_count += 1
            else:
                self.fly_count = 1

        # elif fire:
        #     window.blit(beam[fire_count], (x + 50, y))
        #
        #     if fire_count < 3:
        #         fire_count += 1
        #     else:
        #         fire_count = 3

        else:
            win.blit(char, (self.x, self.y))


def redraw_game_window(ship):

    window.blit(bg, (0, 0))

    ship.draw(win=window)

    pg.display.update()


# Main Loop
run = True
ship = Ship(x=250, y=250, width=32, height=15)

while run:
    clock.tick(30)
    # clock.tick(10)  #  ONLY FOR DEBUG PURPOSE

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

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
