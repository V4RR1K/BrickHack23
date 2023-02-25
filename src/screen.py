import pygame

def init(width, height):
    pygame.init()

    screen = pygame.display.set_mode((width, height))

    # TODO: Game Specifics
    pygame.display.set_caption("Game Name")
    # pygame.display.set_caption("Space Invaders")
    # logo_icon = pygame.image.load('Assets/GameIcon.png')
    # pygame.display.set_icon(logo_icon)

    return screen


def run(screen):
    running = True

    screen.fill((171,219,227))

    # Main Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Closing Game Window")
                break