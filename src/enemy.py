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
        self.icon = icon
        self.current_x = current_x
        self.current_y = current_y
        self.change_in_x = change_in_x
        self.change_in_y = change_in_y
        self.hitbox_rad = hitbox_rad
        self.movement_mod = movement_mod

    def move_to_center(self):
        """
        move_to_center moves the enemy closer to the center
        """
        quadrant = self.detect_quadrant()




    def detect_quadrant(self):
        """
        detects current quadrant where the enemy is and makes a change of location
        :return:
        """
        # Center
        if self.current_x == 400 and self.current_y == 400:
            return 0
        # On Vertical Axis
        if self.current_x == 400:
            if self.current_y > 400:
                return 7
            if self.current_y < 400:
                return 5
        # On Horizontal Axis
        if self.current_y == 400:
            if self.current_x > 400:
                return 8
            if self.current_x < 400:
                return 6
        # Quadrant 1
        if self.current_x > 400 and self.current_y > 400:
            return 1
        # Quadrant 2
        if self.current_x < 400 and self.current_y > 400:
            return 2
        # Quadrant 3
        if self.current_x < 400 and self.current_y < 400:
            return 3
        # Quadrant 4
        if self.current_x > 400 and self.current_y < 400:
            return 4

