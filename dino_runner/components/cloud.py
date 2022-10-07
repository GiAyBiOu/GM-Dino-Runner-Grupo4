from pygame.sprite import Sprite
from utils.constants import CLOUD
import random
class Cloud(Sprite):
    
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        #self.type = random.randint()
        self.cloud_rect.x = 400
        self.cloud_rect.y = 200
    
    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y)) #Blit recibe un objeto tupla, para que se dibuje nuestro objeto
    
    def update(self):
        print()
        if len(self.obstacles) == 0:
            self.obstacles.append(Cloud(CLOUD))
        
        for obstacle in self.obstacles:
            obstacle.update()
            print(obstacle.image_rect.x)
            print(obstacle.image_rect.width)
            if obstacle. image_rect.x < -obstacle. image_rect.width:
                self.obstacles.pop()