import pygame
from pygame.locals import *

import random


class Game:
    def __init__(self):
        self.sw, self.sh = (640, 480)
        self.display = pygame.display.set_mode((self.sw, self.sh))
        self.clock = pygame.time.Clock()
        self.fps = 5
        self.grid_size = 20  # pixels

        self.max_w, self.max_h = (self.sw // self.grid_size, self.sh // self.grid_size)

        self.apple_pos = (0, 0)

        self.colors = {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0)
        }

        self.snake = [
            [0, 0]
        ]

        self.create_apple()


    def adjust_coords(self, coords):
        return (coords[0]*self.grid_size, coords[1]*self.grid_size)


    def create_apple(self):
        self.apple_pos = (random.randint(0, self.max_w), random.randint(0, self.max_h))


    def main(self):
        self.direction = "r"

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    print("key pressed")

                    if event.key == K_UP:
                        self.direction = "u"
                    elif event.key == K_DOWN:
                        self.direction = "d"
                    elif event.key == K_LEFT:
                        self.direction = "l"
                    elif event.key == K_RIGHT:
                        self.direction = "r"
                    print(self.direction)

            if self.direction == "l":
                self.snake[0][0] -= 1
            elif self.direction == "r":
                self.snake[0][0] += 1
            elif self.direction == "u":
                self.snake[0][1] -= 1
            elif self.direction == "d":
                self.snake[0][1] += 1

            self.display.fill(self.colors["BLACK"])

            # draw vertical lines
            for i in range(0, self.sw, self.grid_size):
                pygame.draw.line(self.display, self.colors["WHITE"], (i, 0), (i, self.sh), 3)

            # draw horizontal lines
            for i in range(0, self.sh, self.grid_size):
                pygame.draw.line(self.display, self.colors["WHITE"], (0, i), (self.sw, i), 3)

            pygame.draw.rect(self.display, self.colors["RED"], (self.adjust_coords(self.head_pos), (self.grid_size, self.grid_size)))

            pygame.draw.rect(self.display, self.colors["GREEN"], (self.adjust_coords(self.apple_pos), (self.grid_size, self.grid_size)))

            print(self.head_pos)
            pygame.display.flip()
            self.clock.tick(self.fps)


Game().main()
