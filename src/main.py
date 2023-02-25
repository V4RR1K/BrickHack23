"""
main.py contains the main game method
@date: 02-25-23
@author: Greg Lynskey
"""

import pygame
import screen

window_width = 800
window_height = 800
def main():
    s = screen.init(window_width, window_height)
    screen.run(s)


if __name__ == "__main__":
    main()
