"""
screen.py contains code pertaining to screen specific information
@date: 02-25-23
@author: Greg Lynskey
"""
import numpy
import pygame
import player as p
import enemy as e
import ring as r
import hit_marker as h
import score as s
import assets_generator as ag
import random
import time
import numpy

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

# def load_enemies(time, left, l_c, right, r_c, top, t_c, bottom, b_c, in_play):
#     if time == 1:
#         in_play.append(left[l_c])
#         l_c += 1
#         in_play.append(right[r_c])
#         r_c += 1
#         in_play.append(top[t_c])
#         t_c += 1
#         in_play.append(bottom[b_c])
#         b_c += 1
#     if time == 2:
#         in_play.append(left[l_c])
#         l_c += 1
#         in_play.append(right[r_c])
#         r_c += 1
#         in_play.append(top[t_c])
#         t_c += 1
#         in_play.append(bottom[b_c])
#         b_c += 1

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
    top_arr = list()
    left_arr = list()
    right_arr = list()
    bot_arr = list()
    for i in range(0, 40):
        speed_mod = 100
        # speed_mod = random.randint(100, 150)
        e_t = e.enemy(400, 0, speed_mod)
        top_arr.append(e_t)
        # speed_mod = random.randint(100, 150)
        e_b = e.enemy(400, 800, speed_mod)
        bot_arr.append(e_b)
        # speed_mod = random.randint(100, 150)
        e_r = e.enemy(800, 400, speed_mod)
        right_arr.append(e_r)
        # speed_mod = random.randint(100, 150)
        e_l = e.enemy(0, 400, speed_mod)
        left_arr.append(e_l)


    all_enemies = list()
    all_enemies.extend(top_arr)
    all_enemies.extend(bot_arr)
    all_enemies.extend(right_arr)
    all_enemies.extend(left_arr)

    numpy.random.shuffle(all_enemies)
    timed_enemies = list()

    print(all_enemies)
    significant_times = [7.5, 7.75, 8.0, 8.25, 9, 9.25, 9.75, 10.25, 11, 11.25, 11.75, 12, 12.25,
                         12.25, 12, 13.25, 13.75, 14.25, 15, 15.25, 15.75, 16, 16.25, 17, 17.5,
                         17.75, 18.25, 19, 19.25, 19.75, 20, 20.25, 21, 21.25, 22.25, 23, 23.25,
                         23.75, 24, 24.25, 25, 25.25, 25.75, 26.25, 27, 27.25, 27.75, 28, 28.25, 29,
                         29.25, 29.75, 30.25, 31.25, 31.75, 32, 32.25, 35, 38.25, 38.75, 39.25, 40,
                         40.25, 40.75, 42, 42.25, 43, 43.25, 43.75, 44.25, 44.25, 46.75,
                         49.25, 49.75, 50.25, 51.25, 51.75, 52, 52.25, 55, 58.25, 58.75, 59.25, 60,
                         60.25, 60.75, 62, 62.25, 63, 63.25, 63.75, 64.25, 64.25, 66.75,
                         69.25, 69.75, 70.25, 71.25, 71.75, 72, 72.25, 75
                         ]
    index = 0
    for sig_time in significant_times:
        timed_enemies.append(all_enemies[index].update_spawn(sig_time))
        index += 1
    # top_arr[0].update_spawn(1)
    # bot_arr[0].update_spawn(7.5)
    # right_arr[0].update_spawn(7.75)
    # left_arr[0].update_spawn(8.0)
    # top_arr[1].update_spawn(8.25)
    # bot_arr[1].update_spawn(4)
    # right_arr[1].update_spawn(10)
    # left_arr[1].update_spawn(13)
    # top_arr[2].update_spawn(20)
    # bot_arr[2].update_spawn(18)
    # right_arr[2].update_spawn(19)
    # left_arr[2].update_spawn(17)

    before_play = all_enemies
    in_play = list()

    # Time in seconds
    timer_start = time.perf_counter()
    # Main Game Loop
    while running:
        if player.health == 0:
            screen.blit(ASSET_DICTIONARY["GameOver"], (0,0))

            break
        curr_time = time.perf_counter() - timer_start
        # print(curr_time)

        for enemy in before_play:
            if enemy.spawn_time >= curr_time and enemy.spawn_time <= curr_time + .1:
                enemy.running = True
                in_play.append(enemy)
                before_play.remove(enemy)

                print("Enemy " + str(len(in_play)) + " in play at: " + str(curr_time))


        # Add enemies to screen
        # load_enemies(time, left_arr, l_c, right_arr, r_c, top_arr, t_c, bot_arr, b_c, in_play)

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
                    for enemy in in_play:
                        ring.slash(enemy, player, slash)

                if event.key == pygame.K_LEFT:
                    slash = 2 # Left
                    for enemy in in_play:
                        ring.slash(enemy, player, slash)

                if event.key == pygame.K_UP:
                    slash = 3 # Up
                    for enemy in in_play:
                        ring.slash(enemy, player, slash)

                if event.key == pygame.K_DOWN:
                    slash = 4 # Down
                    for enemy in in_play:
                        ring.slash(enemy, player, slash)

        scoreboard.score_update(player.score)
        scoreboard.score_place(screen)

        dt = game_clock.tick(fps) / 1000  # Update delta time
        # Enemy Placement and hit checking
        for enemy in in_play:
            enemy.enemy_place(screen, dt)
            player.hit_check(enemy, hit_marker)
            if enemy.running is False:
                in_play.remove(enemy)
                print("Enemy out of play at: " + str(curr_time))


        screen.blit(ASSET_DICTIONARY["Circle"], (300,300))
        player.player_place(screen, curr_time)
        ring.ring_place(screen)
        hit_marker.hit_marker_place(screen)
        # End of loop

        pygame.display.update()

    running = True

    while running:
        screen.blit(ASSET_DICTIONARY["GameOver"], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Closing Game Window")
                break
        pygame.display.update()


    print("Player Score: " + str(player.score))
    return 0