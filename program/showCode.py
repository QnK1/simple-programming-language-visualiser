import pygame, config

class ShowCode():
    def __init__(self, simulation):
        self.simulation = simulation
        self.text = ''
        self.begin = 0
        self.end = 0
        self.plain = config.showCode_plain
        self.color = config.showCode_colored
        self.font_size = config.showCode_font_size
        self.width = config.showCode_width
        self.height = config.border_spacing

    def setTest(self, text, begin, end):
        self.text = text
        self.begin = begin
        self.end = end

    def draw(self):
        font = pygame.font.Font(None, self.font_size)
        x = 0
        for i, c in enumerate(self.text):
            color = self.color if i >= self.begin and i < self.end else self.plain
            rendered_char = font.render(c, True, color)
            self.simulation.screen.blit(rendered_char, (self.width + x, self.height))
            x += rendered_char.get_width()

        
