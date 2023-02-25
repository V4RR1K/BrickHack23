"""
Enemy.py holds enemy specific code
@date: 02-25-23
@author: Greg Lynskey
"""
class enemy:
    """
    Enemy class models the enemy attributes
    """
    def __init__(self,
                 icon,
                 current_x,
                 current_y,
                 change_in_x,
                 change_in_y,
                 hitbox_rad,
                 movement_mod):
        self.current_x = current_x
        self.current_y = current_y
        self.change_in_x = change_in_x
        self.change_in_y = change_in_y
        self.hitbox_rad = hitbox_rad
        self.movement_mod = movement_mod

