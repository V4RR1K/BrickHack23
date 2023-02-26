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
import time

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
        speed_mod = random.randint(100, 150)
        e_t = e.enemy(400, 0, speed_mod)
        top_arr.append(e_t)
        speed_mod = random.randint(100, 150)
        e_b = e.enemy(400, 800, speed_mod)
        bot_arr.append(e_b)
        speed_mod = random.randint(100, 150)
        e_r = e.enemy(800, 400, speed_mod)
        right_arr.append(e_r)
        speed_mod = random.randint(100, 150)
        e_l = e.enemy(0, 400, speed_mod)
        left_arr.append(e_l)


    all_enemies = list()
    all_enemies.extend(top_arr)
    all_enemies.extend(bot_arr)
    all_enemies.extend(right_arr)
    all_enemies.extend(left_arr)
    print(all_enemies)

    # top_arr[0].update_spawn(1)
    bot_arr[0].update_spawn(5)
    # right_arr[0].update_spawn(8)
    # left_arr[0].update_spawn(15)
    # top_arr[1].update_spawn(3)
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
        curr_time = time.perf_counter() - timer_start
        # print(curr_time)

        for enemy in before_play:
            if enemy.spawn_time >= curr_time and enemy.spawn_time <= curr_time + .1:
                enemy.running = True
                in_play.append(enemy)
                before_play.remove(enemy)

                print("Enemy in play at: " + str(curr_time))


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

    print("Player Score: " + str(player.score))
    return 0