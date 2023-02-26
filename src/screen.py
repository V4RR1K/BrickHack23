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
import score as s
import assets_generator as ag
import random

random.seed(176)
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

    pygame.display.set_icon(ASSET_DICTIONARY['Logo'])

    pygame.mixer.init()
    pygame.mixer.music.load('assets/music/song1.mp3')
    pygame.mixer.music.play()

    return screen

def run(screen):
    """
    Runs the Game instance
    :param screen: screen to put game on
    :return: 0 on success
    """

    running = True
    screen.blit(ASSET_DICTIONARY['HellBgUp'], (0,0))

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

    # Score
    scoreboard = s.score()

    # Enemy Init (x, y, movement_mod)

    # Top
    top_arr = list()
    for i in range(0, 40):
        speed_mod = random.randint(100, 150)
        e_t = e.enemy(400, 0 ,speed_mod)
        top_arr.append(e_t)

    # Left
    left_arr = list()
    for i in range(0, 40):
        speed_mod = random.randint(100, 150)
        e_l = e.enemy(0, 400, speed_mod)
        left_arr.append(e_l)

    # Bottom
    bot_arr = list()
    for i in range(0, 40):
        speed_mod = random.randint(100, 150)
        e_b = e.enemy(400, 800, speed_mod)
        bot_arr.append(e_b)

    # Right
    right_arr = list()
    for i in range(0, 40):
        speed_mod = random.randint(100, 150)
        e_r = e.enemy(800, 400, speed_mod)
        right_arr.append(e_r)

    all_enemies = list()
    all_enemies.extend(top_arr)
    all_enemies.extend(bot_arr)
    all_enemies.extend(right_arr)
    all_enemies.extend(left_arr)
    print(all_enemies)

    # Time in seconds
    time = 0
    frame_count = 0

    # Main Game Loop
    while running:
        # Timing assist
        frame_count += 1
        if frame_count == 15 and frame_count == 45:
            time += 0.25
        if frame_count == 30:
            time += 0.5
        if frame_count == 60:
            time += 1
            frame_count = 0

        screen.blit(ASSET_DICTIONARY['HellBgUp'], (0,0))

        # Pygame event
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

        scoreboard.score_update(player.score)
        scoreboard.score_place(screen)

        # Enemy Placement and hit checking
        for enemy in all_enemies:
            enemy.enemy_place(screen, dt)
            player.hit_check(enemy, hit_marker)

        screen.blit(ASSET_DICTIONARY["Circle"], (300,300))
        player.player_place(screen, time)
        ring.ring_place(screen)
        hit_marker.hit_marker_place(screen)
        # End of loop
        dt = game_clock.tick(fps) / 1000    # Update delta time
        pygame.display.update()

    print("Player Score: " + str(player.score))
    return 0