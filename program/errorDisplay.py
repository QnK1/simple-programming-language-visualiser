import pygame
from . import config
from .board import Board

class ErrorDisplay:
    def __init__(self, simulation):
        self.simulation = simulation
        self.error_color = config.error_color
        self.error_font_size = config.error_font_size
        self.errors = []
        self.board_offset = config.board_offset
        self.error_line_height = config.error_line_height
        self.error_width_limit = config.error_width_limit

    def displayErrors(self, errors: list):
        self.simulation.boards.append(Board(self.simulation, 'Errors', 0, title_color=config.error_title_color))
        self.errors = errors
    
    def clearErrors(self):
        self.errors = []

    def draw(self):
        lines = 1
        font = pygame.font.Font(None, self.error_font_size)

        for error in self.errors:
            cur_line = ''
            for c in str(error):
                if font.size(cur_line + c)[0] < self.error_width_limit:
                    cur_line += c
                else:
                    error_message = font.render(cur_line, True, self.error_color)
                    self.simulation.screen.blit(error_message, (self.board_offset, self.board_offset + lines * self.error_line_height))
                    lines += 1
                    cur_line = c
            error_message = font.render(cur_line, True, self.error_color)
            self.simulation.screen.blit(error_message, (self.board_offset, self.board_offset + lines * self.error_line_height))
            lines += 1
            
