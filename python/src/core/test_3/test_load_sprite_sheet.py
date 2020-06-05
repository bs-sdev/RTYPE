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

x = 250
y = 250
width = 32
height = 15
vel = 5
is_jump = False
jump_count = 10
left = False
right = False
up = False
down = False
fire = False
fly_count = 0
propellant_count = 3
fire_count = 0


def redraw_game_window():
    global sp_sheet
    global fly_count
    global propellant_count
    global fire_count

    window.blit(bg, (0, 0))

    # img = sp_sheet.get_image(101, 3, 32, 14)
    # img.set_colorkey((0, 0, 0))
    # window.blit(img, (250, 250))

    if fly_count + 1 >= 3:
        fly_count = 0

    if left:
        window.blit(flyLeft[0], (x, y))

    elif right:
        window.blit(propellant[propellant_count], (x - 32, y - 12))
        window.blit(flyRight[0], (x, y))
        if fly_count < 3:
            fly_count += 1
        else:
            fly_count = 1

        if propellant_count > 0:
            propellant_count -= 1
        else:
            propellant_count = 0

    elif up:
        window.blit(flyUp[fly_count], (x, y))
        print("Up N° " + str(fly_count))
        if fly_count < 1:
            fly_count += 1
        else:
            fly_count = 1

    elif down:
        window.blit(flyDown[fly_count], (x, y))
        print("Down N° " + str(fly_count))
        if fly_count < 1:
            fly_count += 1
        else:
            fly_count = 1

    # elif fire:
    #     window.blit(beam[fire_count], (x + 50, y))
    #
    #     if fire_count < 3:
    #         fire_count += 1
    #     else:
    #         fire_count = 3

    else:
        window.blit(char, (x, y))

    pg.display.update()


# Main Loop
run = True

while run:
    clock.tick(30)
    # clock.tick(10)  #  ONLY FOR DEBUG PURPOSE

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pg.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False

    elif keys[pg.K_DOWN] and y < 500 - height - vel:
        y += vel
        up = True
        down = False

    elif keys[pg.K_UP] and y > vel:
        y -= vel
        up = False
        down = True

    elif keys[pg.K_SPACE]:
        fire = True

    else:
        right = False
        left = False
        up = False
        down = False
        fly_count = 0
        propellant_count = 3

    redraw_game_window()

pg.quit()
