from cmath import rect
from components.obstacles.obstacle import Obstacle
import random
class Cactus(Obstacle):
    def __init__(self, image, rect_y =300):
        self.type = random.randint(0, 2)
        self.size = rect_y
        super().__init__(image, self.type)
        self.image_rect.y = self.size

