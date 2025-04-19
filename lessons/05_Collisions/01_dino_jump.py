"""
Dino Jump

Use the arrow keys to move the blue square up and down to avoid the black
obstacles. The game should end when the player collides with an obstacle ...
but it does not. It's a work in progress, and you'll have to finish it. 

"""
import pygame
import random
from pathlib import Path

# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"

# Screen dimensions
class settings:
    WIDTH, HEIGHT = 600, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dino Jump")
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FPS = 60
    OBSTACLE_WIDTH = 20
    OBSTACLE_HEIGHT = 20
    obstacle_speed = 5
    PLAYER_SIZE = 25
    player_speed = 5
    font = pygame.font.SysFont(None, 36)

# Player attributes




# Obstacle attributes


# Font



# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((settings.OBSTACLE_WIDTH, settings.OBSTACLE_HEIGHT))
        self.image.fill(settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = settings.WIDTH
        self.rect.y = settings.HEIGHT - settings.OBSTACLE_HEIGHT - 10

        self.explosion = pygame.image.load(images_dir / "explosion1.gif")

    def update(self):
        self.rect.x -= settings.obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()

    def explode(self):
        """Replace the image with an explosition image."""
        
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (settings.OBSTACLE_WIDTH, settings.OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)


# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((settings.PLAYER_SIZE, settings.PLAYER_SIZE))
        self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = settings.HEIGHT - settings.PLAYER_SIZE - 10
        self.speed = settings.player_speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_SPACE]:
            self.rect.y += self.speed

        # Keep the player on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > settings.HEIGHT:
            self.rect.bottom = settings.HEIGHT

# Create a player object
player = Player()
player_group = pygame.sprite.GroupSingle(player)

# Add obstacles periodically
def add_obstacle(obstacles):
    # random.random() returns a random float between 0 and 1, so a value
    # of 0.25 means that there is a 25% chance of adding an obstacle. Since
    # add_obstacle() is called every 100ms, this means that on average, an
    # obstacle will be added every 400ms.
    # The combination of the randomness and the time allows for random
    # obstacles, but not too close together. 
    
    if random.random() < 0.4:
        obstacle = Obstacle()
        obstacles.add(obstacle)
        return 1
    return 0


# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    game_over = False
    last_obstacle_time = pygame.time.get_ticks()

    # Group for obstacles
    obstacles = pygame.sprite.Group()

    player = Player()

    obstacle_count = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update player
        player.update()

        # Add obstacles and update
        if pygame.time.get_ticks() - last_obstacle_time > 500:
            last_obstacle_time = pygame.time.get_ticks()
            obstacle_count += add_obstacle(obstacles)
        
        obstacles.update()

        # Check for collisions
        collider = pygame.sprite.spritecollide(player, obstacles, dokill=False)
        if collider:
            collider[0].explode()
       
        # Draw everything
        settings.screen.fill(settings.WHITE)
        pygame.draw.rect(settings.screen, settings.BLUE, player)
        obstacles.draw(settings.screen)

        # Display obstacle count
        obstacle_text = settings.font.render(f"Obstacles: {obstacle_count}", True, settings.BLACK)
        settings.screen.blit(obstacle_text, (10, 10))

        pygame.display.update()
        clock.tick(settings.FPS)

    # Game over screen
    settings.screen.fill(settings.WHITE)

if __name__ == "__main__":
    game_loop()
