import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
GRAVITY = 0.5
JUMP_VELOCITY = -10
MOVEMENT_SPEED = 5  # Adjust movement speed as needed
FPS = 60
RAIN_DELAY = 3000  # Delay for 3 seconds (in milliseconds)
MAX_RAIN_PARTICLES = 10  # Maximum number of raindrops
COUNTDOWN_FONT_SIZE = 120  # Font size for countdown
SCORE_FONT_SIZE = 60  # Font size for score

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load images
player_image = pygame.image.load("CUEIORight.png")
background_image = pygame.image.load("Papel-de-Parede.jpg.webp")
raindrop1_image = pygame.image.load("decio__.png")
raindrop2_image = pygame.image.load("lilou__.png")

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Presente Dia dos Namorados")

# Load sound
pygame.mixer.music.load("cute-level-up-3-189853.mp3")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.velocity = 0
        self.score = 0
        self.moving_left = False
        self.moving_right = False

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        if self.moving_left:
            self.rect.x -= MOVEMENT_SPEED
        if self.moving_right:
            self.rect.x += MOVEMENT_SPEED

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0

    def jump(self):
        self.velocity = JUMP_VELOCITY

    def increase_score(self):
        self.score += 1
        pygame.mixer.music.play()  # Play sound when score increases

# Raindrop class
class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([raindrop1_image, raindrop2_image])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-HEIGHT, 0)
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.image = random.choice([raindrop1_image, raindrop2_image])

# Function to render text onto the screen
def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Create sprite groups
all_sprites = pygame.sprite.Group()
raindrops = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Variables to track the delay for countdown
start_time = pygame.time.get_ticks()
countdown_started = True
countdown_duration = 3000  # Countdown duration (in milliseconds)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_RIGHT:
                player.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_RIGHT:
                player.moving_right = False

    # Update
    all_sprites.update()

    # Create raindrops continuously
    if pygame.time.get_ticks() - start_time >= RAIN_DELAY:
        # Create raindrops
        if len(raindrops) < MAX_RAIN_PARTICLES:
            raindrop = Raindrop()
            all_sprites.add(raindrop)
            raindrops.add(raindrop)

    # Check for collisions between player and raindrops
    collisions = pygame.sprite.spritecollide(player, raindrops, True)
    if collisions:
        player.increase_score()

    # Draw
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Draw countdown timer if countdown is active
    if countdown_started:
        countdown_remaining = max(0, (countdown_duration - (pygame.time.get_ticks() - start_time)) // 1000 + 1)
        countdown_font = pygame.font.Font(None, COUNTDOWN_FONT_SIZE)
        draw_text(str(countdown_remaining), countdown_font, RED, screen, WIDTH // 2, HEIGHT // 2)

    # Draw score
    score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
    draw_text("Pontos: " + str(player.score), score_font, RED, screen, 20, 20)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
