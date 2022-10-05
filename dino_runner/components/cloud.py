from pygame.sprite import Sprite
from utils.constants import CLOUD

class Cloud(Sprite):
    
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = 400
        self.cloud_rect.y = 200
    
    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y)) #Blit recibe un objeto tupla, para que se dibuje nuestro objeto
        #homework