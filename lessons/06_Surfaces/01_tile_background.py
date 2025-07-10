"""
Example of loading a background image that is not as wide as the screen, and
tiling it to fill the screen.

"""
import pygame


# Initialize Pygame
pygame.init()

from pathlib import Path
assets = Path(__file__).parent / 'images'
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)


# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Background')
def make_rectangle():
    pygame.Rect(1, 1, 100, 100)
test = pygame.Rect(1, 1, 100, 600)
test2 = pygame.Rect(100, 1, 100, 600)
test3 = pygame.Rect(200, 1, 100, 600)
test4 = pygame.Rect(300, 1, 100, 600)
test5 = pygame.Rect(400, 1, 100, 600)
test6 = pygame.Rect(500, 1, 100, 600)

    
    
def maketiledcolors(screen):
    pygame.Surface.fill((255, 0, 0), rect=None, special_flags=0)

def make_tiled_bg(screen, bg_file):
    # Scale background to match the screen height
    
    bg_tile = pygame.image.load(bg_file).convert()
    
    background_height = screen.get_height()
    bg_tile = pygame.transform.scale(bg_tile, (bg_tile.get_width(), screen.get_height()))

    # Get the dimensions of the background after scaling
    background_width = bg_tile.get_width()

    # Make an image the is the same size as the screen
    image = pygame.Surface((screen.get_width(), screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), background_width):
        image.blit(bg_tile, (x, 0))
        
    return image

background = make_tiled_bg(screen, assets/'background_tile.gif')
make_rectangle()
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    pygame.draw.rect(screen, WHITE, test)
    pygame.draw.rect(screen, RED, test2)
    pygame.draw.rect(screen, BLUE, test3)
    pygame.draw.rect(screen, PURPLE, test4)
    pygame.draw.rect(screen, BLACK, test5)
    pygame.draw.rect(screen, GREEN, test6)
    
    

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
