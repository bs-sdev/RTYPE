######################################################################################
# Tutorial video taken:
#   - https://www.youtube.com/watch?v=UdsNBIzsmlI
######################################################################################

import os
import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("R-Type (The original)")

flyRight = [
    pygame.image.load(os.path.join("../sprites", 'standing.png'))
]

flyLeft = [
    pygame.image.load(os.path.join("../sprites", 'standing.png'))
]

flyDown = [
    pygame.image.load(os.path.join("../sprites", 'down_1.png')),
    pygame.image.load(os.path.join("../sprites", 'down_2.png'))
]

flyUp = [
    pygame.image.load(os.path.join("../sprites", 'up_1.png')),
    pygame.image.load(os.path.join("../sprites", 'up_2.png'))
]

beam = [
    pygame.image.load(os.path.join("../sprites", '.png'))
]

bg = pygame.image.load(os.path.join("../sprites", "SpaceBackground1.png"))
char = pygame.image.load(os.path.join("../sprites", 'standing.png'))

clock = pygame.time.Clock()

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
fly_count = 0


def redraw_game_window():
    global fly_count
    window.blit(bg, (0, 0))

    # Attention, originellement, c'est dans le cas d'un array de 9 sprites avec 3 frames par sprite (3 * 9)
    if fly_count + 1 >= 3:
        fly_count = 0

    if left:
        window.blit(flyLeft[0], (x, y))

    elif right:
        window.blit(flyRight[0], (x, y))

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
    else:
        window.blit(char, (x, y))

    pygame.display.update()


# Main Loop
run = True

while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False

    elif keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel
        up = True
        down = False

    elif keys[pygame.K_UP] and y > vel:
        y -= vel
        up = False
        down = True

    else:
        right = False
        left = False
        up = False
        down = False
        fly_count = 0

    redraw_game_window()

pygame.quit()















