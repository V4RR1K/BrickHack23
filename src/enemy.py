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
                 movement_mod):
        self.icon = icon
        self.current_x = current_x
        self.current_y = current_y
        self.change_in_x = 0
        self.change_in_y = 0
        self.hitbox_rad = 32
        self.movement_mod = movement_mod

    def enemy_place(self, screen, dt):
        self.move_to_center(dt)
        screen.blit(self.icon, (self.current_x, self.current_y))

    def move_to_center(self, dt):
        """
        move_to_center moves the enemy closer to the center
        """
        quadrant = self.detect_quadrant()

        # Determine move
        match(quadrant):
            case 0: # At origin
                self.change_in_y = 0
                self.change_in_x = 0
            case 5:     # Coming from top
                self.change_in_y = 1 * self.movement_mod
            case 6:     # Coming from left
                self.change_in_x = 1 * self.movement_mod
            case 7:     # Coming from bottom
                self.change_in_y = -1 * self.movement_mod
            case 8:     # Coming from left
                self.change_in_x = -1 * self.movement_mod

        # Make the move
        self.current_x += self.change_in_x * dt
        self.current_y += self.change_in_y * dt

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

        # Approaching on Diagonal
        # # Quadrant 1
        # if self.current_x > 400 and self.current_y > 400:
        #     return 1
        # # Quadrant 2
        # if self.current_x < 400 and self.current_y > 400:
        #     return 2
        # # Quadrant 3
        # if self.current_x < 400 and self.current_y < 400:
        #     return 3
        # # Quadrant 4
        # if self.current_x > 400 and self.current_y < 400:
        #     return 4

