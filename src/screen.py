"""
screen.py contains code pertaining to screen specific information
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import player as p
import enemy as e
import ring as r
import hit_marker as h
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

    pygame.display.set_icon(ASSET_DICTIONARY['BlobBig'])

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
    player = p.player()

    # Ring Init
    ring = r.ring()

    # Hit Marker Init
    hit_marker = h.hit_marker()

    # Enemy Init (png, x, y, movement_mod)

    # Top
    e_1 = e.enemy(400, 0, 60)
    top_arr = list()
    top_arr.append(e_1)
    # Left
    e_2 = e.enemy(0, 400, 175)
    left_arr = list()
    left_arr.append(e_2)
    # Bottom
    e_3 = e.enemy(400, 800, 100)
    bot_arr = list()
    bot_arr.append(e_3)
    # Right
    e_4 = e.enemy(800, 400, 130)
    right_arr = list()
    right_arr.append(e_4)

    all_enemies = list()
    all_enemies.extend(top_arr)
    all_enemies.extend(bot_arr)
    all_enemies.extend(right_arr)
    all_enemies.extend(left_arr)
    print(all_enemies)

    # Main Game Loop
    while running:

        screen.fill((171, 219, 227))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Closing Game Window")
                break
            # Slash Code
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    slash = 1 # Right
                    for enemy in all_enemies:
                        ring.slash(enemy, player, slash)

                if event.key == pygame.K_LEFT:
                    slash = 2 # Left
                    for enemy in all_enemies:
                        ring.slash(enemy, player, slash)

                if event.key == pygame.K_UP:
                    slash = 3 # Up
                    for enemy in all_enemies:
                        ring.slash(enemy, player, slash)

                if event.key == pygame.K_DOWN:
                    slash = 4 # Down
                    for enemy in all_enemies:
                        ring.slash(enemy, player, slash)

        player.player_place(screen)

        # Enemy Placement and hit checking
        for enemy in all_enemies:
            enemy.enemy_place(screen, dt)
            player.hit_check(enemy, hit_marker)




        ring.ring_place(screen)
        hit_marker.hit_marker_place(screen)
        # End of loop
        dt = game_clock.tick(fps) / 1000    # Update delta time
        pygame.display.update()

    print("Player Score: " + str(player.score))
    return 0