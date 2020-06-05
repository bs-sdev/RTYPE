# import pygame
#
#
# # define a main function
# def main():
#     # initialize the pygame module
#     pygame.init()
#     # load and set the logo
#     logo = pygame.image.load("../sprites/SpaceBackground1.png")
#     pygame.display.set_icon(logo)
#     pygame.display.set_caption("minimal program")
#
#     # create a surface on screen that has the size of 240 x 180
#     screen = pygame.display.set_mode((1280, 720))
#
#     # define a variable to control the main loop
#     running = True
#
#     # main loop
#     while running:
#         # event handling, gets all event from the event queue
#         for event in pygame.event.get():
#             # only do something if the event is of type QUIT
#             if event.type == pygame.QUIT:
#                 # change the value to False, to exit the main loop
#                 running = False
#
#
# # run the main function only if this module is executed as the main script
# # (if you import this as a module then nothing is executed)
# if __name__=="__main__":
#     # call the main function
#     main()
import os

import pygame
import sys
from pygame.locals import *

pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))

# os.path.join properly forms a cross-platform relative path
# by joining directory names
bg = pygame.image.load(os.path.join("../sprites", "SpaceBackground1.png"))


pygame.mouse.set_visible(0)


pygame.display.set_caption('galaxy invaders')

while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
