# kekueater.py
# player will eat cake heehoo

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "kekueater"
NUM_FOOD = 50

# TODO: replace blocks with cakes
# TODO: player must eat cake - add score in the end
# TODO: Change player movements to keyboard
# TODO: add bad food that makes player lose a life or end game
# TODO : possibly put in an enemy class


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/cake.png")
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.image.load("./images/piglet.png")
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()

    def update(self):
        """Move player with the mouse"""
        self.rect.center = pygame.mouse.get_pos()




def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()


    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()

    # make lots of blocks on the screen
    for i in range(NUM_FOOD):
        food = Food()
        food.rect.y = random.randrange(HEIGHT - food.rect.height)
        food.rect.x = random.randrange(WIDTH - food.rect.width)
        all_sprites.add(food)
        block_sprites.add(food)

    player = Player()
    all_sprites.add(player)
    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()
        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)



        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
