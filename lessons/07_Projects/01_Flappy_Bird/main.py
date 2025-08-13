import pygame
import random
from pathlib import Path

assets = Path(__file__).parent / "images"

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy bird")

player_speed = 5
PLAYER_SIZE = 25

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(assets/'bluebird-downflap.png')
        print(self.image.get_rect())
        self.image = pygame.transform.scale(self.image,(25, 25))
        #self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - PLAYER_SIZE - 10
        self.speed = player_speed
        
        
        
      

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_SPACE] and self.rect.bottom == HEIGHT:
            self.speed = -5.8
        
        
        self.rect.y += self.speed
        self.speed += .37

        # Keep the player on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

if __name__ == "__main__":
    while True:
        from pathlib import Path
        assets = Path(__file__).parent / 'images'
        background = pygame.image.load(assets/'background.png')
        
        background = pygame.transform.scale(background, (WIDTH/3, HEIGHT))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        background = pygame.transform.scale(background, (WIDTH/3, HEIGHT))
        screen.blit(background, (200, 0))
        pygame.display.flip()
        background = pygame.transform.scale(background, (WIDTH/3, HEIGHT))
        screen.blit(background, (400, 0))
        pygame.display.flip()


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
       