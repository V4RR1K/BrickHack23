"""
score.py holds score of player
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
class score:
    def _init__(self):
        self.score_num = 0

    def score_place(self, screen):
        score_font = pygame.font.Font('freesansbold.ttf', 32)
        score_str = "Score: " + str(self.score_num)
        text = score_font.render(score_str, True, (255,255,255))
        screen.blit(text, (20, 20))

    def score_update(self, new_score):
        self.score_num = new_score