# dvdblock.py
# Initial goal: get a block moving on the screen
#   * x and y direction
#   * modify its velocity
# Stretch goal: replace the vlock ith an image of the dvd logo (like the office segment)

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "DVD Image"

# class to represent rhe DVD Block
#   * location in space
#   * size
#   * colour
class Block():
    def __init__(self):
        # initial location in the middle
        self.x, self.y = (WIDTH/2, HEIGHT/2)
        self.width, self.height = (125, 100)
        self.colour = (SKY_BLUE)
        self.x_vel = 7
        self.y_vel = 0


    def update(self):
        """updates the x- and y- location of the block based on its x_vel and y_vel

        Returns: None
        """
        self.x += self.x_vel
        self.y += self.y_vel

        # TODO: Bounce the block when it reached the sides
        # TODO: for x
        # if x + self.width > WIDTH --> x_vel * -1
        if self.x < 0 or self.x + self.width > WIDTH:
            self.x_vel *= -1
        # TODO: y direction
        if self.y < 0 or self.y + self.height > HEIGHT:
            self.y_vel *= -1


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    block = Block()
    second_block = Block()
    second_block.colour = YELLOW
    second_block.y_vel = random.choice([-4, -2, 2, 4])
    second_block.x_vel = random.choice([-4, -2, 2, 2])


    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
       # update the block's location
        block.update()
        second_block.update()



        # ----- DRAW
        screen.fill(BLACK)
        pygame.draw.rect(
            screen,
            block.colour,
            [
                block.x,
                block.y,
                block.width,
                block.height,
            ]
        )
        pygame.draw.rect(
            screen,
            second_block.colour,
            [
                second_block.x,
                second_block.y,
                second_block.width,
                second_block.height,
            ]
        )
        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
