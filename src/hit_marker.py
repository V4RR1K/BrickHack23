"""
hit_marker.py holds hit marker specific code
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import enemy
import assets_generator as a

dictionary = a.generate_assets_dir("z_hit_marker")
class hit_marker:
    """
    Hit Marker class models the hit marker attributes
    """
    def __init__(self):

        self.icon = dictionary["Hit_Marker_1"]
        self.current_x = 750 - 32
        self.current_y = 50 - 32

    def hit_marker_place(self, screen):
        screen.blit(self.icon, (self.current_x, self.current_y))

    def hit_marker_decrease(self, player):
        match(player.health):
            case 5:
                self.icon = dictionary["Hit_Marker_1"]
            case 4:
                self.icon = dictionary["Hit_Marker_2"]
            case 3:
                self.icon = dictionary["Hit_Marker_3"]
            case 2:
                self.icon = dictionary["Hit_Marker_4"]
            case 1:
                self.icon = dictionary["Hit_Marker_5"]




