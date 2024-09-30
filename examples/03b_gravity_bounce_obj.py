"""
Gravity bounce in Object Oriented style

This version of the gravity bounce program uses an object oriented style to
organize the code. The main game loop is in the Game class, and the player is
a separate class. This makes the code easier to read and understand, and
allows for more complex games with multiple objects.

"""
import pygame
from dataclasses import dataclass
from enum import Enum


# Here is an eample of using the class to store costants directly, 
# without creating an instance of the class. 
class Colors:
    """Constants for Colors"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)


@dataclass
class GameSettings:
    """Settings for the game"""
    width: int = 500
    height: int = 500
    gravity: float = 0.3
    player_start_x: int = 100
    player_start_y: int = None
    player_v_y: float = 0 # Initial y velocity
    player_v_x: float = 7 # Initial x velocity
    player_width: int = 20
    player_height: int = 20
    player_jump_velocity: float = 15

class Game:
    """Main object for the top level of the game. Holds the main loop and other
    update, drawing and collision methods that operate on multiple other
    objects, like the player and obstacles."""
    
    def __init__(self, settings: GameSettings):
        
        # Notice that we are passing settings into the Game object, but we are not
        # passing in Colors. This is jus a stylistic choice; the Colors could be
        # part of the settings, or passed in as a separate object.

        pygame.init()

        self.settings = settings
        self.running = True

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.clock = pygame.time.Clock()

    def run(self):
        """Main game loop"""

        player = Player(self)

        while self.running:

            # Hitting a key or clicking the close button or hitting the ESC key
            # will generate an event that we can capture and use to end the game
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            player.update()

            self.screen.fill(Colors.WHITE)
            player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


class Player:
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game):
        
        self.game = game
        settings = game.settings

        self.width = settings.player_width
        self.height = settings.player_height
      
        self.is_jumping = False
        self.v_jump = settings.player_jump_velocity

        # Recalc Y since we don't know size in the default arg list. 
        self.y = settings.player_start_y if settings.player_start_y is not None else settings.height - self.height

        self.x = settings.player_start_x
        
        self.v_x = settings.player_v_x # X Velocity
        self.v_y = settings.player_v_y # Y Velocity

    # This is the main update method for the player. It is called every frame
    # and updates the player's position based on gravity and velocity.
    # Notice that we've broken the update method into smaller methods to make
    # it easier to read and understand. This is a good practice for any method
    # that does more than one thing
    def update(self):
        """Update player position, continuously jumping"""
        self.update_jump()
        self.update_y()
        self.update_x()

    def update_y(self):
        """Update the player's y position based on gravity and velocity"""
        self.v_y += self.game.settings.gravity  # Add gravity to the y velocity
        self.y += self.v_y  # Update the player's y position, based on the current velocity

        # If the player hits the ground, stop the player from falling.
        if self.y >= self.game.settings.height - self.height:
            self.y = self.game.settings.height - self.height
            self.v_y = 0
            self.is_jumping = False

    def update_x(self):
        """Update the player's x position based on horizontal velocity and bounce on edges"""
        self.x += self.v_x  # Update the player's x position based on the current velocity

        # If the player hits the left or right edge, reverse the horizontal velocity
        if self.x <= 0:
            self.x = 0
            self.v_x = -self.v_x
        elif self.x >= self.game.settings.width - self.width:
            self.x = self.game.settings.width - self.width
            self.v_x = -self.v_x

    def update_jump(self):
        """Handle the player's jumping logic"""
        
        # Notice that the vertical motion of the player is not really a bounce;
        # the player touches the ground and stops, then that triggers another jump 
        if not self.is_jumping:
            self.v_y = -self.v_jump
            self.is_jumping = True

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.BLACK, (self.x, self.y, self.width, self.height))


settings = GameSettings()
game = Game(settings)
game.run()