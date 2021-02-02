# do_nut_eat.py
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
NUM_FOOD = 70
MAX_VEGGIE = 7


# TODO: Change player movements to keyboard
# TODO: veggie that makes player lose a life or end game
print("Hello, your goal is to eat cake. Don't eat the vegetables or you'll lose 5 points! Your goal is to eat 50 donuts")



class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("images/donut.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.image.load("images/piglet.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)

    def update(self):
        """Move player with the mouse"""
        self.rect.center = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.image.load("images/lakitu.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (650, 500)
        self.x_vel = 3
        self.y_vel = 3

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Keep inside the screen and bounce back
        if self.rect.x < 0 or self.rect.x + self.rect.width > WIDTH:
            self.x_vel *= -1
        if self.rect.y < 0 or self.rect.y + self.rect.height > HEIGHT:
            self.y_vel *= -1

class Veggie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.image.load("./images/carrot.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.y_vel = 2

        # randomize location
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, HEIGHT)

    def update(self):
        self.rect.y += self.y_vel

        # if the carrot reaches the bottom, reset its position
        if self.rect.y > HEIGHT:
            self.rect.y = random.randrange(-15, 0)

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
    score_c = 0

    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    veggie_sprites = pygame.sprite.Group()



    # make lots of donuts on the screen
    for i in range(NUM_FOOD):
        food = Food()
        food.rect.y = random.randrange(HEIGHT - food.rect.height)
        food.rect.x = random.randrange(WIDTH - food.rect.width)
        all_sprites.add(food)
        block_sprites.add(food)
    # player
    player = Player()
    all_sprites.add(player)
    # enemy
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

    # make some veggies
    veggie_list = []
    for i in range(MAX_VEGGIE):
        veggie = Veggie()
        veggie_list.append(veggie)
        all_sprites.add(veggie)
        veggie_sprites.add(veggie)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()

        # When the player class eats the food class
        block_hit_list = pygame.sprite.spritecollide(player, block_sprites, True)
        for block in block_hit_list:
            score += 1
            print(score)
        if score == 50:
            print("You win!")
            quit()



        # When the player hits the enemy
        enemy_hit_player = pygame.sprite.spritecollide(player, enemy_sprites, True)
        for player in enemy_hit_player:
            print("game over. Lakitu caught you! Please try again :)")
            quit()

        # When the player eats the veggies
        veggie_hit_player = pygame.sprite.spritecollide(player, veggie_sprites, True)
        for veggie in veggie_hit_player:
            score -= 5
            print(f"You ate a carrot! You lost 5 points. You have {score} donuts")
        for veggie in veggie_hit_player:
            score_c += 1
        if score_c > 4:
            print("You ate too many carrots!")
            quit()


        # ----- DRAW
        screen.fill(SKY_BLUE)
        block_sprites.draw(screen)
        enemy_sprites.draw(screen)
        all_sprites.draw(screen)
        veggie_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()