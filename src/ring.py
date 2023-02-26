"""
ring.py holds ring of harmony specific code
@date: 02-25-23
@author: Greg Lynskey
"""
import assets_generator as a
import pygame

class ring:
    """
    Ring class models the player attributes
    """
    def __init__(self):
        dictionary = a.generate_assets_dir("z_const")
        self.icon = dictionary["Ring_of_Harmony"]
        self.current_x = 300
        self.current_y = 300
        self.hitbox_rad = 200

    def ring_place(self, screen):
        screen.blit(self.icon, (self.current_x ,self.current_y))

    def slash(self, enemy, player, slash_code):
        if (enemy.current_y <= 315 and enemy.current_y > 300) \
                and enemy.quadrant == 5 \
                and enemy.isSlashed is False:
            player.score += 15
            print("hit")
            enemy.isSlashed = True
        # if enemy.current_x > 315 \
        #         and enemy.quadrant == 6 \
        #         and enemy.did_damage is False:
        #     enemy.did_damage = True
        #     self.health -= 1
        #     hit_marker.hit_marker_decrease(self)
        # if enemy.current_y < 485 \
        #         and enemy.quadrant == 7 \
        #         and enemy.did_damage is False:
        #     enemy.did_damage = True
        #     self.health -= 1
        #     hit_marker.hit_marker_decrease(self)
        # if enemy.current_x < 485 \
        #         and enemy.quadrant == 8 \
        #         and enemy.did_damage is False:
        #     enemy.did_damage = True
        #     self.health -= 1
        #     hit_marker.hit_marker_decrease(self)


