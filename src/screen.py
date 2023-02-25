"""
screen.py contains code pertaining to screen specific information
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import player as p
import enemy as e
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
    """
    Runs the Game instance
    :param screen: screen to put game on
    :return: 0 on success
    """

    running = True
    asset_dict = ag.generate_assets()
    screen.fill((171,219,227))

    # FPS Settings
    fps = 60
    dt = 0
    game_clock = pygame.time.Clock()
    game_clock.tick(fps)


    # Player Init
    player = p.player(asset_dict["player_icon"],
                      400, 400, 40, 0, 20)

    # Enemy Init (png, x, y, movement_mod)
    e_1 = e.enemy(asset_dict["enemy1_icon"], 0, 400, 100)

    # Main Game Loop
    while running:

        screen.fill((171, 219, 227))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Closing Game Window")
                break

        player.player_place(screen)

        # Enemy Bounds
        e_1.enemy_place(screen, dt)

        # End of loop
        dt = game_clock.tick(fps) / 1000    # Update delta time
        pygame.display.update()

    return 0