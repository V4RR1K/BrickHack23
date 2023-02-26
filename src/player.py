"""
player.py holds player specific code
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import enemy
import hit_marker
import assets_generator as a
dictionary = a.generate_assets_dir("z_const")
class player:
    """
    Player class models the player attributes
    """
    def __init__(self):
        self.icon = dictionary['DaBaby1']
        self.current_x = 400 - 32
        self.current_y = 400 - 32
        self.hitbox_rad = 32
        self.score = 0
        self.health = 5
        self.flip = 0
        self.icon_num = 1


    def player_place(self, screen, time):
        self.flip += 1
        if self.flip == 60:
            match(self.icon_num):
                case 1:
                    self.icon = dictionary['DaBaby2']
                    self.icon_num = 2
                    self.flip = 0
                case 2:
                    self.icon = dictionary['DaBaby1']
                    self.icon_num = 1
                    self.flip = 0
            self.flip += 1
        screen.blit(self.icon, (self.current_x, self.current_y))

    def hit_check(self, enemy, hit_marker):
        """
        hit_check checks if enemy hits player
        :param enemy: current enemy being checked
        :param hit_marker: current hit marker to update
        """
        if enemy.current_y > 325 \
                and enemy.quadrant == 5 \
                and enemy.did_damage is False\
                and enemy.isSlashed is False:
            enemy.did_damage = True
            self.health -= 1
            hit_marker.hit_marker_decrease(self)
        if enemy.current_x > 325 \
                and enemy.quadrant == 6 \
                and enemy.did_damage is False\
                and enemy.isSlashed is False:
            enemy.did_damage = True
            self.health -= 1
            hit_marker.hit_marker_decrease(self)
        if enemy.current_y < 475 \
                and enemy.quadrant == 7 \
                and enemy.did_damage is False\
                and enemy.isSlashed is False:
            enemy.did_damage = True
            self.health -= 1
            hit_marker.hit_marker_decrease(self)
        if enemy.current_x < 475 \
                and enemy.quadrant == 8 \
                and enemy.did_damage is False\
                and enemy.isSlashed is False:
            enemy.did_damage = True
            self.health -= 1
            hit_marker.hit_marker_decrease(self)


