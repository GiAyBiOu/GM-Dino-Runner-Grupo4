
from cgitb import small
from email.mime import image
from components.obstacles.cactus import Cactus
import pygame 
import random

from utils.constants import (
    LARGE_CACTUS, SMALL_CACTUS
)
class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(1 , 2)
            if cactus_size == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_size == 2:
                small_cactus = Cactus(SMALL_CACTUS)
                small_cactus.image_rect.y = 320
                self.obstacles.append(small_cactus)
        for obstacle in self.obstacles:
            obstacle.update()
            #print(obstacle.image_rect.x)
            #print(obstacle.image_rect.width)
            if obstacle. image_rect.x < -obstacle. image_rect.width:
                self.obstacles.pop()
            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(500)
                game.death_count += 1
                self.obstacles.pop()
                if game.death_count == 5:
                    game.playing = False
                    game.excute()
                print(game.death_count)
                


