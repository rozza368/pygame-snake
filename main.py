import pygame
from pygame.locals import *

import random
import copy


class Game:
    def __init__(self):
        self.sw, self.sh = (640, 480)
        self.display = pygame.display.set_mode((self.sw, self.sh))
        self.clock = pygame.time.Clock()
        self.fps = 8
        self.grid_size = 20  # pixels

        self.points = 0

        self.max_w, self.max_h = (self.sw // self.grid_size, self.sh // self.grid_size)

        self.colors = {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0)
        }

        self.snake = [
            [4, 4],
            [3, 4],
            [2, 4]
        ]

        self.create_apple()


    def adjust_coords(self, coords):
        return (coords[0]*self.grid_size, coords[1]*self.grid_size)


    def create_apple(self):
        while True:
            self.apple_pos = [random.randint(0, self.max_w-1), random.randint(0, self.max_h-1)]
            if not self.apple_pos in self.snake:
                break
    

    def game_over(self, reason=""):
        # placeholder
        print(f"Game over! {reason}")
        pygame.quit()
        exit()


    def main(self):
        keep_last = False
        draw_grid = False
        self.direction = "r"

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP and not self.direction == "d":
                        self.direction = "u"
                    elif event.key == K_DOWN and not self.direction == "u":
                        self.direction = "d"
                    elif event.key == K_LEFT and not self.direction == "r":
                        self.direction = "l"
                    elif event.key == K_RIGHT and not self.direction == "l":
                        self.direction = "r"

            self.display.fill(self.colors["BLACK"])

            # which direction the snake should go, change the head
            new_head = copy.deepcopy(self.snake)[0]
            
            if self.direction == "l":
                new_head[0] -= 1
            elif self.direction == "r":
                new_head[0] += 1
            elif self.direction == "u":
                new_head[1] -= 1
            elif self.direction == "d":
                new_head[1] += 1
            
            self.snake.insert(0, new_head)
            if not keep_last:
                del self.snake[-1]
            keep_last = False

            snake_head = self.snake[0]
            # apple collision
            if snake_head == self.apple_pos:
                self.points += 1
                self.create_apple()
                keep_last = True
            

            # self collision
            if snake_head in self.snake[2:]:
                print(self.snake[0], self.snake[1:])
                self.game_over("Collided with self.")
            

            # edge collision

            if snake_head[0] < 0 or snake_head[1] < 0 or snake_head[0] > self.max_w or snake_head[1] > self.max_h:
                self.game_over("Went out of bounds.")


            ### START DRAWING
            if draw_grid:
                # draw vertical lines
                for i in range(0, self.sw, self.grid_size):
                    pygame.draw.line(self.display, self.colors["WHITE"], (i, 0), (i, self.sh), 2)

                # draw horizontal lines
                for i in range(0, self.sh, self.grid_size):
                    pygame.draw.line(self.display, self.colors["WHITE"], (0, i), (self.sw, i), 2)

            # draw snake
            for segment in self.snake:
                pygame.draw.rect(self.display, self.colors["RED"], (self.adjust_coords(segment), (self.grid_size, self.grid_size)))

            # draw apple
            pygame.draw.rect(self.display, self.colors["GREEN"], (self.adjust_coords(self.apple_pos), (self.grid_size, self.grid_size)))

            ### END DRAWING

            # print(self.snake[0], self.apple_pos)
            pygame.display.flip()
            self.clock.tick(self.fps)



Game().main()
