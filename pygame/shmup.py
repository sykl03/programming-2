# shmup.py
# top down shoot em up (shmup game)
# get more comfortable with sprites and mouse
# creation of new sprite objects in the main loop
# using pygame.mouse a little more comfortably

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 720
HEIGHT = 1280
TITLE = "The Shmup"

# class player, enemies, bullets
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/Galaga_ship.png")
        self.rect = self.image.get_rect()

    def update(self):
        """Move the player with the mouse"""
        self.rect.center = pygame.mouse.get_pos()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/Mario.png")
        self.rect = self.image.get_rect()
        self.x_vel = 3
    def update(self):
        self.rect.x += self.x_vel

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_vel *= 1


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprites = pygame.sprite.Group() # to draw
    enemy_sprites = pygame.sprite.Group() # enemies

    # Populate sprite groups
    enemy = Enemy()
    enemy.rect.y = 150
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

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
