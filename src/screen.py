"""
screen.py contains code pertaining to screen specific information
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import player as p
import assets_generator as ag

def init(width, height):
    """
    Initializes the window    :
    :param width:  Width
    :param height: window Height
    :return: pygame display
    """
    pygame.init()

    screen = pygame.display.set_mode((width, height))

    # TODO: Game Specifics
    pygame.display.set_caption("Game Name")
    # logo_icon = pygame.image.load('Assets/GameIcon.png')
    # pygame.display.set_icon(logo_icon)

    return screen


def run(screen):
    running = True
    asset_dict = ag.generate_assets()
    screen.fill((171,219,227))

    # Player init
    player = p.player(asset_dict["player_icon"],
                      400, 400, 40, 0, 20)

    # Main Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Closing Game Window")
                break
        player.player_place(screen)
        pygame.display.update()