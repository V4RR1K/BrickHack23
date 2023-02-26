"""
player.py holds player specific code
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import enemy
import hit_marker
import assets_generator as a
class player:
    """
    Player class models the player attributes
    """
    def __init__(self):
        dictionary = a.generate_assets_dir("z_const")
        self.icon = dictionary["Player"]
        self.current_x = 400 - 32
        self.current_y = 400 - 32
        self.hitbox_rad = 32
        self.score = 0
        self.health = 5

    def player_place(self, screen):
        screen.blit(self.icon, (self.current_x, self.current_y))

    def hit_check(self, enemy, hit_marker):
        if enemy.current_x < 315 and enemy.quadrant == 6:
            self.health -= 1
            hit_marker.hit_marker_decrease(self)


