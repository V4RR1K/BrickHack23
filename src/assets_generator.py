"""
assets_generator.py loads assets into python code
@date: 02-25-23
@author: Greg Lynskey
"""
import pygame
import os

def generate_all_static_assets():
    blue = generate_assets_dir("blue")
    green = generate_assets_dir("green")
    red = generate_assets_dir("red")
    yellow = generate_assets_dir("yellow")
    const = generate_assets_dir("z_const")
    hit = generate_assets_dir("z_hit_marker")

    all = dict()
    all |= blue
    all |= green
    all |= red
    all |= yellow
    all |= const
    all |= hit
    # print(all)
    return all
def generate_all_enemy_assets():
    blue = generate_assets_dir("blue")
    green = generate_assets_dir("green")
    red = generate_assets_dir("red")
    yellow = generate_assets_dir("yellow")

    all = dict()
    all |= blue
    all |= green
    all |= red
    all |= yellow
    # print(all)
    return all
def generate_static_assets():
    gen_asset_path = 'assets/static/'
    asset_dictionary = dict()
    for file in os.listdir(gen_asset_path):
        asset_path = os.path.join(gen_asset_path, file)
        # print(asset_path)
        asset_dictionary[file[:len(file)-4]] = pygame.image.load(asset_path)
    # print(asset_dictionary)
    return asset_dictionary
def generate_assets_dir(dir):
    match(dir):
        case "red":
            gen_asset_path = 'assets/static/red/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                # print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            # print(asset_dictionary)
            return asset_dictionary
        case "blue":
            gen_asset_path = 'assets/static/blue/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                # print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            # print(asset_dictionary)
            return asset_dictionary
        case "green":
            gen_asset_path = 'assets/static/green/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                # print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            # print(asset_dictionary)
            return asset_dictionary
        case "yellow":
            gen_asset_path = 'assets/static/yellow/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                # print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            # print(asset_dictionary)
            return asset_dictionary
        case "z_const":
            gen_asset_path = 'assets/static/z_const/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                # print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            # print(asset_dictionary)
            return asset_dictionary
        case "z_hit_marker":
            gen_asset_path = 'assets/static/z_hit_marker/'
            asset_dictionary = dict()
            for file in os.listdir(gen_asset_path):
                asset_path = os.path.join(gen_asset_path, file)
                # print(asset_path)
                asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
            # print(asset_dictionary)
            return asset_dictionary


def main():
    generate_assets_dir("yellow")
    generate_all_static_assets()

if __name__ == "__main__":
    main()