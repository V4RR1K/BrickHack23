"""
ring.py holds ring of harmony specific code
@date: 02-25-23
@author: Greg Lynskey
"""
class ring:
    """
    Ring class models the player attributes
    """
    def __init__(self,
                 icon,
                 current_x,
                 current_y,
                 hitbox_rad):
        self.icon = icon
        self.current_x = current_x
        self.current_y = current_y
        self.hitbox_rad = hitbox_rad

