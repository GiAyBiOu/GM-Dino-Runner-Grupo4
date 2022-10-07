from cgitb import text
from email import message
from turtle import update
import pygame
from components.dinosaur import Dinosaur
from components.cloud import Cloud
from components.obstacles.obstacle_manager import ObstacleManager
from utils.constants import RUNNING
from utils import text_utils
from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_running = True
        self.dino = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.points = 0

    def run(self):
        # Game loop: events - update - draw
        self.reset_attributes()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
    
    def reset_attributes(self):
        self.playing = True
        self.death_count = 0
        self.points = 0
    
    def excute(self):
        while self.game_running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dino.update(user_input)
        self.obstacle_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.score()
        self.dino.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1 
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        self.show_menu_options()
        pygame.display.update()
        self.handle_events_menu()
        
    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 self.run()
            if event.type == pygame.QUIT:
                 self.game_runnig = False
                 self.playing = False
                 pygame.display.quit()
                 pygame.quit()
                 exit()
    
    def show_menu_options(self):
        message = "Welcome to Dino Runner Game" if self.death_count <= 0 else "Game Over !!!"
        text, text_rect = text_utils.get_centered_message(message , font_size=30)
        self.screen.blit(text, text_rect)
        pos_Y = (SCREEN_HEIGHT // 2) + 30
        message_instruction = "Press any key to start the game" if self.death_count <= 0 else "Press any key to play again"
        text_instruction, text_instruction_rect = text_utils.get_centered_message(message_instruction , height=pos_Y)
        self.screen.blit(text_instruction, text_instruction_rect)
        self.screen.blit(RUNNING[0], ((SCREEN_WIDTH // 2), pos_Y - 150))
