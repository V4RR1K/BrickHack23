"""
assets_generator.py loads assets into python code
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import os

def generate_assets_manual():
    """
    Generates all the assets into pygame images
    :return: asset dictionary
    """


    player_icon = pygame.image.load('assets/static/Player.png')
    enemy1_icon = pygame.image.load('assets/static/Enemy1.png')
    nunes = pygame.image.load('assets/static/Nunes.png')

    return {"player_icon": player_icon,
            "enemy1_icon": enemy1_icon,
            "nunes": nunes}

def generate_assets():
    gen_asset_path = 'assets/static/'
    asset_dictionary = dict()
    for file in os.listdir(gen_asset_path):
        asset_path = os.path.join(gen_asset_path, file)
        asset_dictionary[file[:len(file)-4]] = pygame.image.load(asset_path)
    print(asset_dictionary)

def main():
    generate_assets()

if __name__ == "__main__":
    main()