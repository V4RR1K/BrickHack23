"""
main.py contains the main game method
@date: 02-25-23
@author: Greg Lynskey
"""


import pygame_menu
import screen

window_width = 800
window_height = 800

def level_one():
    s = screen.init(window_width, window_height)
    screen.run(s, 1)

def level_two():
    s = screen.init(window_width, window_height)
    screen.run(s, 1)
def main():
    s = screen.init(window_width, window_height)
    menu = pygame_menu.Menu("Katabasis", 800, 800, theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Level 1', level_one)
    menu.add.button('Level 2', level_two)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(s)


if __name__ == "__main__":
    main()
