"""
screen.py contains code pertaining to screen specific information
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import player as p
import enemy as e
import assets_generator as ag

ASSET_DICTIONARY = ag.generate_all_static_assets()
def init(width, height):
    """
    Initializes the window    :
    :param width:  Width
    :param height: window Height
    :return: pygame display
    """
    pygame.init()

    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Katabasis")

    pygame.display.set_icon(ASSET_DICTIONARY['Nunes'])

    return screen

def run(screen):
    """
    Runs the Game instance
    :param screen: screen to put game on
    :return: 0 on success
    """

    running = True
    screen.fill((171,219,227))

    # FPS Settings
    fps = 60
    dt = 0
    game_clock = pygame.time.Clock()
    game_clock.tick(fps)


    # Player Init
    player = p.player(ASSET_DICTIONARY["Player"],
                      400, 400, 40, 0, 20)

    # Enemy Init (png, x, y, movement_mod)

    # Top
    e_1 = e.enemy(400, 0, 100)
    # Left
    e_2 = e.enemy(0, 400, 100)
    # Bottom
    e_3 = e.enemy(400, 800, 100)
    # Right
    e_4 = e.enemy(800, 400, 100)

    # Main Game Loop
    while running:

        screen.fill((171, 219, 227))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Closing Game Window")
                break

        player.player_place(screen)

        # Enemy Placement
        e_1.enemy_place(screen, dt)
        e_2.enemy_place(screen, dt)
        e_3.enemy_place(screen, dt)
        e_4.enemy_place(screen, dt)


        # End of loop
        dt = game_clock.tick(fps) / 1000    # Update delta time
        pygame.display.update()

    return 0