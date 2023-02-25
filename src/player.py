"""
player.py holds player specific code
@date: 02-25-23
@author: Greg Lynskey
"""
class player:
    """
    Player class models the player attributes
    """
    def __init__(self,
                 icon,
                 current_x,
                 current_y,
                 hitbox_rad,
                 score,
                 health):
        self.icon = icon
        self.current_x = current_x
        self.current_y = current_y
        self.hitbox_rad = hitbox_rad
        self.score = score
        self.health = health

    def player_place(self, screen):
        screen.blit(self.icon, (self.current_x, self.current_y))
