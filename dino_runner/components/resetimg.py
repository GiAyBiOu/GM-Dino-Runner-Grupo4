from pygame.sprite import Sprite
from utils.constants import RESET

class Reset(Sprite):
    X_POS = 500
    Y_POS = 350

    def __init__(self):
        self.image = RESET
        self.reset_rect = self.image.get_rect()
        self.reset_rect.x = self.X_POS
        self.reset_rect.y = self.Y_POS

    def draw(self, screen):
        screen.blit(self.image, (self.reset_rect.x, self.reset_rect.y))