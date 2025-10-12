import pygame
import math
from pathlib import Path
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 200, 200
FPS = 60
assets = Path(__file__).parent / "images"
images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WIDTH, HEIGHT = 600, 300
PLAYER_SIZE = 25
player_speed = 5
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(assets/'spaceship.png')
        print(self.image.get_rect())
        self.image = pygame.transform.scale(self.image,(25, 25))
        #self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - PLAYER_SIZE - 10
        self.speed = player_speed
player = Player()
group = pygame.sprite.Group()
group.add(player)
#def main():
    # Initial position of the square
    #square_x = SCREEN_WIDTH // 2 - SQUARE_SIZE // 2
    #square_y = SCREEN_HEIGHT // 2 - SQUARE_SIZE // 2
    
running = True
    
while running:
        

    # Event handling
    for event in pygame.event.get():
            
        # Check for clicking the close button
        if event.type == pygame.QUIT:
            running = False
    group.draw(screen)
    screen.fill((255, 0, 0))
        
        # Get the keys pressed. Gtes an array of all the keys
        # with a boolean value of whether they are pressed or not
