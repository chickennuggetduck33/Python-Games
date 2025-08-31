"""
Dino Jump

Use the arrow keys to move the blue square up and down to avoid the black
obstacles. The game should end when the player collides with an obstacle ...
but it does not. It's a work in progress, and you'll have to finish it. 

"""



import pygame
import random
from pathlib import Path
from random import randint


assets = Path(__file__).parent / "images"
score = 0
highscore = 0

# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"

# Screen dimensions
class settings:
    WIDTH, HEIGHT = 600, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("flappy bird")
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (0, 0, 255)
    FPS = 60
    obstacle_speed = 5
    PLAYER_SIZE = 25
    player_speed = 5
    font = pygame.font.SysFont(None, 36)
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 500
OBSTACLE_HEIGHT2 = 1000
# Player attributes

 




# Obstacle attributes


# Font

def gethighscore():
    with open("/workspaces/Python-Games/lessons/05_Collisions/highscore.txt", "r") as file:
        content = file.read()
    return int(content)
def savehighscore(highscore):
    with open("/workspaces/Python-Games/lessons/05_Collisions/highscore.txt", "w") as file:
        file.write(str(highscore))
    

# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, random.randint(20, 300)))
        self.image.fill(settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = settings.WIDTH
        self.rect.y = settings.HEIGHT - OBSTACLE_HEIGHT - 50

        self.explosion = pygame.image.load(images_dir / "explosion1.gif")
        self.cactus = pygame.image.load(images_dir / "pipe-green.png")

        self.image = self.cactus
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        global score
        self.rect.x -= settings.obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()
            score +=1
            #print(score)

    def explode(self):
        """Replace the image with an explosition image."""
        global score
        global highscore
        global game_over
        
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)
        print(highscore)
        print(score)
        if highscore < score:
            highscore = score
            savehighscore(highscore)
        #print(highscore)
        score = 0
        self.kill()
        game_over = True
        return True
    



class Obstacle2(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((OBSTACLE_WIDTH, random.randint(20, 100)))
            self.image.fill(settings.BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = settings.WIDTH
            self.rect.y = settings.HEIGHT - OBSTACLE_HEIGHT + 900

            self.explosion = pygame.image.load(images_dir / "explosion1.gif")
            self.cactus = pygame.image.load(images_dir / "pipe-green.png")

            self.image = self.cactus
            self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT2))
            self.rect = self.image.get_rect(center=self.rect.center)

        def update(self):
            global score
            self.rect.x -= settings.obstacle_speed
            # Remove the obstacle if it goes off screen
            if self.rect.right < 0:
                self.kill()
                score +=1
                #print(score)

        def explode(self):
            """Replace the image with an explosition image."""
            global score
            global highscore
            global game_over
            
            # Load the explosion image
            self.image = self.explosion
            self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
            self.rect = self.image.get_rect(center=self.rect.center)
            print(highscore)
            print(score)
            if highscore < score:
                highscore = score
                savehighscore(highscore)
            #print(highscore)
            score = 0
            self.kill()
            game_over = True
            return True
        


# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(assets/'bluebird-downflap.png')
        print(self.image.get_rect())
        self.image = pygame.transform.scale(self.image,(25, 25))
        #self.image.fill(settings.BLUE)
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
            self.speed = -5.8
        
        
        self.rect.y += self.speed
        self.speed += .37

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
        obstacle2 = Obstacle2()
        obstacles.add(obstacle2)
        return 1
    return 0
highscore = gethighscore()

# Main game loop
def game_loop():
    
    clock = pygame.time.Clock()
    game_over = False
    last_obstacle_time = pygame.time.get_ticks()

    
    # Group for obstacles
    obstacles = pygame.sprite.Group()

    player = Player()
    playergroup = pygame.sprite.Group()
    playergroup.add(player)
    obstacle_count = 0

    gameoverbutton = pygame.Rect(100, 100, 150, 150)
    restarttext = settings.font.render(f"restart", True, settings.BLACK)

    

    while True:
        if not game_over:
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
                game_over = True
                
        
            # Draw everything
            settings.screen.fill(settings.RED)
            #pygame.draw.rect(settings.screen, settings.BLUE, player)
            obstacles.draw(settings.screen)
            playergroup.draw(settings.screen)

            # Display obstacle count
            
            obstacle_text = settings.font.render(f"Obstacles: {obstacle_count}", True, settings.BLACK)
            settings.screen.blit(obstacle_text, (10, 10))
            score_text = settings.font.render(f"score: {int(score)}", True, settings.BLACK)
            settings.screen.blit(score_text, (400, 10))
            highscore_text = settings.font.render(f"high score: {int(highscore)}", True, settings.BLACK)
            settings.screen.blit(highscore_text, (400, 30))

        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0]> gameoverbutton.x and mouse[0] < gameoverbutton.x + gameoverbutton.width:
                    if mouse[1]> gameoverbutton.y and mouse[1] < gameoverbutton.y + gameoverbutton.height:
                        game_over = False
                        obstacle_count = 0
                        obstacles.empty()

            settings.screen.fill(settings.BLACK)
            pygame.draw.rect(settings.screen, settings.WHITE, gameoverbutton)
            settings.screen.blit(restarttext, (100, 100))
        

        pygame.display.update()
        clock.tick(settings.FPS)
    # Game over screen
    
    

if __name__ == "__main__":
    game_loop()
