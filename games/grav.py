import pygame
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRAVITY_CONSTANT = 0.0001  # Gravity constant, tweak for better effect
PLAYER_RADIUS = 15
JUMP_VELOCITY = 10  # Jump velocity for spacebar jump
PLAYER_MASS = 1
PLANET_MASSES = [1000, 800, 600]  # Masses of the planets
PLANET_RADII = [50, 60, 40]  # Radii of the planets
PLANET_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Colors of planets

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Jumping Gravity System")

# Define Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.on_planet = None  # Keeps track of the planet the player is on

    def apply_gravity(self, planets):
        gravity_force_x = 0
        gravity_force_y = 0

        # Loop through planets and apply gravity
        for (planet_x, planet_y, mass, radius) in planets:
            dx = self.x - planet_x
            dy = self.y - planet_y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            # Apply gravity if the player is not on the surface of the planet
            if distance > radius + PLAYER_RADIUS:
                force = GRAVITY_CONSTANT * PLAYER_MASS * mass / distance**2
                force_x = force * (dx / distance)
                force_y = force * (dy / distance)

                gravity_force_x += force_x
                gravity_force_y += force_y

        # Apply gravity to player velocity
        self.vel_x += gravity_force_x
        self.vel_y += gravity_force_y

    def move(self):
        # Update position based on velocity
        self.x += self.vel_x
        self.y += self.vel_y

    def land_on_planet(self, planet):
        # Check if the player is on the planet's surface
        dx = self.x - planet.x
        dy = self.y - planet.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < planet.radius + PLAYER_RADIUS:
            normal_x = dx / distance  # Direction to the planet's center (normalized)
            normal_y = dy / distance
            self.x = planet.x + normal_x * (planet.radius + PLAYER_RADIUS)  # Land on the surface
            self.y = planet.y + normal_y * (planet.radius + PLAYER_RADIUS)
            self.vel_x = 0  # Stop horizontal velocity
            self.vel_y = 0  # Stop vertical velocity
            return True  # Player has landed
        return False

    def apply_input(self, keys):
        # Keyboard input for movement (WASD or Arrow keys)
        move_speed = 3  # Speed the player can move on the planet
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -move_speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = move_speed
        else:
            self.vel_x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel_y = -move_speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel_y = move_speed
        else:
            self.vel_y = 0

    def jump(self, direction_x, direction_y):
        # Simulate a jump in the direction of the mouse (escape gravity)
        self.vel_x += direction_x * JUMP_VELOCITY
        self.vel_y += direction_y * JUMP_VELOCITY

# Define Planet class
class Planet:
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create planets
planets = [
    Planet(300, 400, PLANET_RADII[0], PLANET_MASSES[0], PLANET_COLORS[0]),
    Planet(500, 300, PLANET_RADII[1], PLANET_MASSES[1], PLANET_COLORS[1]),
    Planet(200, 200, PLANET_RADII[2], PLANET_MASSES[2], PLANET_COLORS[2])
]

# Create player
player = Player(WIDTH // 2, HEIGHT // 2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard input for movement
    keys = pygame.key.get_pressed()

    # Apply movement input
    player.apply_input(keys)

    # Apply gravity from all planets
    player.apply_gravity([(planet.x, planet.y, planet.mass, planet.radius) for planet in planets])

    # Check if the player has landed on any planet
    landed = False
    for planet in planets:
        if player.land_on_planet(planet):
            landed = True

    # If the player is not landed, apply movement based on gravity
    if not landed:
        player.move()

    # Jumping with Spacebar when landed on a planet
    if landed and pygame.key.get_pressed()[pygame.K_SPACE]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - player.x
        dy = mouse_y - player.y
        distance = math.sqrt(dx**2 + dy**2)

        # Jump in the direction of the mouse (if within a reasonable range)
        if distance < 300:  # Jump only if the mouse is within 300px
            normal_x = dx / distance
            normal_y = dy / distance
            player.jump(normal_x, normal_y)

    # Draw planets
    for planet in planets:
        planet.draw()

    # Draw the player
    pygame.draw.circle(screen, (255, 255, 255), (int(player.x), int(player.y)), PLAYER_RADIUS)

    # Update the display
    pygame.display.flip()

    # Set frame rate
    clock.tick(60)

pygame.quit()
