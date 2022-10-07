from pygame.sprite import Sprite
from utils.constants import GAMEOVER

class GameOver(Sprite):
    X_POS = 350
    Y_POS = 300

    def __init__(self):
        self.image = GAMEOVER
        self.gameo_rect = self.image.get_rect()
        self.gameo_rect.x = self.X_POS
        self.gameo_rect.y = self.Y_POS

    def draw(self, screen):
        screen.blit(self.image, (self.gameo_rect.x, self.gameo_rect.y))