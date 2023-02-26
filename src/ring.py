"""
ring.py holds ring of harmony specific code
@date: 02-25-23
@author: Greg Lynskey
"""
import assets_generator as a


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

