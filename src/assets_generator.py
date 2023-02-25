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

def generate_static_assets():
    gen_asset_path = 'assets/static/'
    asset_dictionary = dict()
    for file in os.listdir(gen_asset_path):
        asset_path = os.path.join(gen_asset_path, file)
        print(asset_path)
        asset_dictionary[file[:len(file)-4]] = pygame.image.load(asset_path)
    print(asset_dictionary)
    return asset_dictionary

def generate_assets_dir(dir):
    match(dir):
        case "red":
            gen_asset_path = 'assets/static/red/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            print(asset_dictionary)
            return asset_dictionary
        case "blue":
            gen_asset_path = 'assets/static/blue/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            print(asset_dictionary)
            return asset_dictionary
        case "green":
            gen_asset_path = 'assets/static/green/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            print(asset_dictionary)
            return asset_dictionary
        case "yellow":
            gen_asset_path = 'assets/static/yellow/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            print(asset_dictionary)
            return asset_dictionary


def main():
    generate_assets_dir("yellow")

if __name__ == "__main__":
    main()