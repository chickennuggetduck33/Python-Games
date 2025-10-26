import pygame
import math
import random
from pathlib import Path
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 60
assets = Path(__file__).parent / "images"
images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_SIZE = 75
ENEMY_SPEED = 1
HEIGHT = 75
player_speed = 1
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(assets/'spaceship.png')
        print(self.image.get_rect())
        self.image = pygame.transform.scale(self.image,(75, 75))
        #self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 262.5
        self.rect.y = HEIGHT - PLAYER_SIZE + 400
        self.speed = player_speed
player = Player()
group = pygame.sprite.Group()
group.add(player)
#def main():
    # Initial position of the square
    #square_x = SCREEN_WIDTH // 2 - SQUARE_SIZE // 2
    #square_y = SCREEN_HEIGHT // 2 - SQUARE_SIZE // 2
EX = random.randint(0, SCREEN_WIDTH - PLAYER_SIZE)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(assets/'alien.png')
        print(self.image.get_rect())
        self.image = pygame.transform.scale(self.image,(75, 75))
        #self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = EX
        self.rect.y = 200
        self.speed = ENEMY_SPEED
enemy = Enemy()
Egroup = pygame.sprite.Group()
Egroup.add(enemy)
running = True
    
while running:
        

    # Event handling
    for event in pygame.event.get():
            
        # Check for clicking the close button
        if event.type == pygame.QUIT:
            running = False
    group.draw(screen)
    screen.fill((0, 0, 155))
    group.draw(screen)
    Egroup.draw(screen)
    enemy.rect.y += enemy.speed
    player.rect.x = max(0, min(SCREEN_WIDTH - PLAYER_SIZE, player.rect.x))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.rect.x += player_speed
    pygame.display.flip()
    
    
        
        # Get the keys pressed. Gtes an array of all the keys
        # with a boolean value of whether they are pressed or not
