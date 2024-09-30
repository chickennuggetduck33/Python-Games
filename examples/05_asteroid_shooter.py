"""

This really boring asteroids game doesn't have any asteroids! It's just a
triangle that can shoot red missles. However, it does have some interesting
features: it uses the Vector2 class from Pygame to handle the player's position
and the projectiles' directions, and it uses the rotate method to rotate the
triangle and the projectiles.


"""
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Really Boring Asteroids")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Triangle settings
TRIANGLE_SIZE = 20
player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
player_angle = 0

# Projectile settings
projectiles = []
PROJECTILE_SPEED = 5

# Clock
clock = pygame.time.Clock()
FPS = 60

# Function to draw the triangle
def draw_triangle(surface: pygame.surface.Surface, position: pygame.Vector2, angle: float):
    
    # Define the triangle's points relative to its center. This triangle is
    # just pointing stright up. 
    points = [
        pygame.Vector2(0, -TRIANGLE_SIZE), # top point
        pygame.Vector2(-TRIANGLE_SIZE / 2, TRIANGLE_SIZE), # left side point
        pygame.Vector2(TRIANGLE_SIZE / 2, TRIANGLE_SIZE) # right side point
    ]
    
    # Rotate the points around the center to the desired angle, then move the
    # triangle to the desired position by adding the position vector to each
    # point
    rotated_points = [point.rotate(angle) + position for point in points]
    pygame.draw.polygon(surface, WHITE, rotated_points)

# Function to move projectiles
def move_projectiles():
    for projectile in projectiles[:]:
        projectile["pos"] += projectile["direction"] * PROJECTILE_SPEED
        # Remove projectiles that are out of bounds
        if not (0 <= projectile["pos"].x <= WIDTH) or not (0 <= projectile["pos"].y <= HEIGHT):
            projectiles.remove(projectile)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new projectile
                direction = pygame.Vector2(0, -1).rotate(player_angle)
                
                # When we create a new projectile, 
                projectile = {
                    "pos": player_pos.copy(),
                    "direction": direction
                }
                
                projectiles.append(projectile)

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle -= 5
    if keys[pygame.K_RIGHT]:
        player_angle += 5

    # Move projectiles
    move_projectiles()

    # Drawing
    screen.fill(BLACK)
    draw_triangle(screen, player_pos, player_angle)

    # Draw projectiles
    for projectile in projectiles:
        pygame.draw.circle(screen, RED, (int(projectile["pos"].x), int(projectile["pos"].y)), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()