import pygame
from . import config

class ButtonDisplay():
    def __init__(self, simulation):
        self.simulation = simulation
        self.font_size = config.button_font_size
        self.offset_x = config.button_offset_x
        self.offset_y = config.button_offset_y
        self.button_color = config.button_color
        self.width = config.button_width
        self.height = config.button_height
        self.spacing = config.button_spacing
        self.text_color = config.button_text_color
        self.text_offset_x = config.button_text_offset_x
        self.text_offset_y = config.button_text_offset_y

    def drawExecuteButton(self):
        font = pygame.font.SysFont(None, self.font_size)                    
        button_rect = pygame.Rect(self.offset_x, self.offset_y, self.width, self.height)
        button_text = font.render("Wykonaj", True, self.text_color)
        pygame.draw.rect(self.simulation.screen, self.button_color, button_rect)
        self.simulation.screen.blit(button_text, (button_rect.x + self.text_offset_x, button_rect.y + self.text_offset_y))

    def drawPauseButton(self):
        font = pygame.font.SysFont(None, self.font_size)                    
        button_rect = pygame.Rect(self.offset_x + self.width*1 + self.spacing, self.offset_y, self.width, self.height)
        button_text = font.render("Pauza", True, self.text_color)
        pygame.draw.rect(self.simulation.screen, self.button_color, button_rect)
        self.simulation.screen.blit(button_text, (button_rect.x + self.text_offset_x, button_rect.y + self.text_offset_y))

    def draw(self):
        self.drawExecuteButton()