"""
screen.py contains code pertaining to screen specific information
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import player

def init(width, height):
    pygame.init()

    screen = pygame.display.set_mode((width, height))

    # TODO: Game Specifics
    pygame.display.set_caption("Game Name")
    # logo_icon = pygame.image.load('Assets/GameIcon.png')
    # pygame.display.set_icon(logo_icon)

    return screen


def run(screen):
    running = True

    screen.fill((171,219,227))

    player =

    # Main Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Closing Game Window")
                break