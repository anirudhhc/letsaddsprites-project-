import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)  # Black background

# Sprite dimensions
RECT_WIDTH = 50
RECT_HEIGHT = 50
SPRITE_COLOR_1 = (255, 0, 0)  # Red
SPRITE_COLOR_2 = (0, 0, 255)  # Blue

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game with Two Sprites')

# Define the clock object
clock = pygame.time.Clock()

# Initial positions of the sprites
sprite1_pos = [100, 100]
sprite2_pos = [600, 400]

# Speed of the moving sprite
sprite_speed = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the first sprite with arrow keys
    if keys[pygame.K_LEFT]:
        sprite1_pos[0] -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite1_pos[0] += sprite_speed
    if keys[pygame.K_UP]:
        sprite1_pos[1] -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite1_pos[1] += sprite_speed

    # Ensure sprite1 stays on the screen
    sprite1_pos[0] = max(0, min(SCREEN_WIDTH - RECT_WIDTH, sprite1_pos[0]))
    sprite1_pos[1] = max(0, min(SCREEN_HEIGHT - RECT_HEIGHT, sprite1_pos[1]))

    # Fill the screen with the background color
    screen.fill(BG_COLOR)

    # Draw the sprites
    pygame.draw.rect(screen, SPRITE_COLOR_1, (*sprite1_pos, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(screen, SPRITE_COLOR_2, (*sprite2_pos, RECT_WIDTH, RECT_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
random.exit()