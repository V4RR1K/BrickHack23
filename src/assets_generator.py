"""
assets_generator.py loads assets into python code
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame

def generate_assets():
    """
    Generates all the assets into pygame images
    :return: asset dictionary
    """
    player_icon = pygame.image.load('assets/Player.png')
    enemy1_icon = pygame.image.load('assets/Enemy1.png')
    nunes = pygame.image.load('assets/Nunes.png')

    return {"player_icon": player_icon,
            "enemy1_icon": enemy1_icon,
            "nunes": nunes}