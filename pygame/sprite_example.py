# Sprite_example.py
# replace our classes with sprites
# Goals: to introduce sprite class. subclass the sprite class

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1024
HEIGHT = 768
TITLE = "Sprite Example"
NUM_BLOCKS = 105

class Block(pygame.sprite.Sprite):
    def __init__(self):
        # call the superclass constructor
        super().__init__()

        # Image
        self.image = pygame.Surface((35, 20))
        self.image.fill((0, 255, 0))

        # rectangle (x, y, width, height)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.image.load("./images/link.png")

        # rect
        self.rect = self.image.get_rect()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, size = 5):
      self.colour = WHITE
      self.size = size
      self.x = random.randrange(0, WIDTH)
      self.y = random.randrange(0, HEIGHT)
      self.x_vel = 4
      self.y_vel = 3

      self.image = pygame.Surface((35, 20))
      self.image.fill((255, 0, 0))
      self.circle = self.image.get_rect()

    def update(self):
        """move player with the mouse"""
        #pygame.mouse.get_pos()
        self.rect.center = pygame.mouse.get_pos()

        # move the enemy
        #self.x += self.x_vel
        #self.y += self.y_vel


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    score = 0

    # create a group of sprites for all sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # make lots of blocks on the screen
    for i in range(NUM_BLOCKS):
        block = Block()
        block.rect.x = random.randrange(WIDTH-block.rect.width)
        block.rect.y = random.randrange(HEIGHT-block.rect.height)
        all_sprites.add(block)
        block_sprites.add(block)

    player = Player()
    all_sprites.add(player)

    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)


    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()

        # sprite group that has the sprites collided with
        block_hit_list = pygame.sprite.spritecollide(player, block_sprites, True)
        for block in block_hit_list:
            score += 1
            print(score)
        # ----- DRAW

        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
