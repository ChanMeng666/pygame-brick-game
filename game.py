import pygame
import sys

# Introduction of font module
import pygame.freetype

# Introducing message alert boxes
import tkinter as tk
from tkinter import messagebox

# Initialising Pygame
pygame.init()

# screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hit the Bricks")

# Colour definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]  # 彩虹色


# frame rate
clock = pygame.time.Clock()


def show_messagebox(message):
    root = tk.Tk()
    root.withdraw()  # Hide main window
    return messagebox.askyesno("prompt", message)

if not show_messagebox("Game on. Are you ready?"):
    pygame.quit()
    sys.exit()

# Reset the game
def reset_game():
    global ball, paddle, all_sprites, bricks, game_over
    all_sprites = pygame.sprite.Group()
    bricks = pygame.sprite.Group()

    ball = Ball()
    paddle = Paddle()
    all_sprites.add(ball)
    all_sprites.add(paddle)

    for i in range(16):
        for j in range(14):
            brick = Brick(50 * i, 20 * j, COLORS[j % 7])
            all_sprites.add(brick)
            bricks.add(brick)

    game_over = False

# ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        pygame.draw.circle(self.image, WHITE, (5, 5), 5)  # draw a circle
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.speed = [5, 5]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]

# board type
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 550

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

# bricks
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([50, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Creating a sprite group
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

# Creating ball and board
ball = Ball()
paddle = Paddle()
all_sprites.add(ball)
all_sprites.add(paddle)

# Creating Bricks
for i in range(16):  # Modify the number of bricks to fill the screen
    for j in range(14):
        brick = Brick(50 * i, 20 * j, COLORS[j % 7])  # Modify the colour of the bricks to form a rainbow-coloured arrangement
        all_sprites.add(brick)
        bricks.add(brick)

# The main game loop
running = True
game_over = False
font = pygame.freetype.Font(None, 36)  # Creating a Font Object
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Ball and Board Collision Detection
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed[1] = -ball.speed[1]

    # Ball and Bricks Collision Detection
    brick_collisions = pygame.sprite.spritecollide(ball, bricks, True)
    if brick_collisions:
        ball.speed[1] = -ball.speed[1]

    # Game Over Detection
    if ball.rect.bottom >= 600:
        game_over = True

    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Game Over Tips
    if game_over:
        font.render_to(screen, (350, 300), "Game Over", WHITE)

        pygame.display.flip()
        if not show_messagebox("Game over. Is there another game?"):
            pygame.quit()
            sys.exit()
        else:
            reset_game()

    if not bricks:  # If there are no more bricks, the game is won
        font.render_to(screen, (350, 300), "Congratulations on your victory.", WHITE)
        pygame.display.flip()
        if not show_messagebox("Congratulations on your victory. Would you like to play another round?"):
            pygame.quit()
            sys.exit()
        else:
            reset_game()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
