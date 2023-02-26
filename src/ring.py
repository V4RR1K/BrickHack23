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

    def slash(self, enemy, player, slash_code):
        slash_hit = False
        # Right
        if (enemy.current_x <= 525 and enemy.current_x > 485) \
                and enemy.quadrant == 8 \
                and enemy.isSlashed is False\
                and slash_code == 1:
            player.score += 15
            print("hit")
            enemy.isSlashed = True
            slash_hit = True
        # Left
        if (enemy.current_x <= 325 - 32 and enemy.current_x > 290 - 32) \
                and enemy.quadrant == 6 \
                and enemy.isSlashed is False \
                and slash_code == 2:
            player.score += 15
            print("hit")
            enemy.isSlashed = True
            slash_hit = True
        # Top
        if (enemy.current_y <= 325 - 32 and enemy.current_y > 290 - 32) \
                and enemy.quadrant == 5 \
                and enemy.isSlashed is False \
                and slash_code == 3:
            player.score += 15
            print("hit")
            enemy.isSlashed = True
            slash_hit = True
        # Bottom
        if (enemy.current_y <= 525 and enemy.current_y > 475) \
                and enemy.quadrant == 7 \
                and enemy.isSlashed is False \
                and slash_code == 4:
            player.score += 15
            print("hit")
            enemy.isSlashed = True
            slash_hit = True

        if slash_hit is False:
            player.score -= 1



