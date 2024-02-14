import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Presente Dia dos Namorados")

# Load the background image
background_image = pygame.image.load("C:\Users\lecio\diaDosNamorados\Papel-de-Parede.jpg.webp")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Define colors
BLUE = (0, 0, 255)
NAVY_BLUE = (0, 0, 128)

# Load the player's image from the same directory
player_image = pygame.image.load("CUEIORight.png")
player_width, player_height = player_image.get_width(), player_image.get_height()
player_x, player_y = (WIDTH - player_width) // 2, (HEIGHT - player_height) // 2

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the player's image
    screen.blit(player_image, (player_x, player_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
