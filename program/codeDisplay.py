import pygame

class CodeDisplay():
    def __init__(self, simulation):
        self.simulation = simulation
    def draw(self):
        font = pygame.font.SysFont(None, 36)                    
        button_rect = pygame.Rect(1000, 120, 100, 50)
        button_text = font.render("Kliknij", True, (0,0,0))
        pygame.draw.rect(self.simulation.screen, (0,0,155), button_rect)
        self.simulation.screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))