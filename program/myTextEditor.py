from pathlib import Path
from . import config
from pygame_texteditor import TextEditor
from interface.get_pygments_tokens import SyntaxHighlighter
import pygame

class MyTextEditor:
    def __init__(self, simulation):
        self.arrowX = -50
        self.arrowY = -50
        self.simulation = simulation
        self.offset_x=config.editor_offset_x
        self.offset_y=config.editor_offset_y
        self.font_size=config.editor_font_size

        self.TX = TextEditor(offset_x=self.offset_x, offset_y=self.offset_y, editor_width=config.editor_width,
                                editor_height=config.editor_height, screen=self.simulation.screen)
        self.TX.set_line_numbers(True)
        self.TX.lexer = SyntaxHighlighter()
        self.TX.set_syntax_highlighting(True)
        self.TX.set_colorscheme_from_yaml(Path(__file__).resolve().parent / Path("colors.yaml"))
        self.TX.set_font_size(self.font_size)
        self.TX.set_text_from_string('\n\n\n\n\n')
        self.allowWrite = True

    def allowWriting(self):
        self.allowWrite = True
    
    def arrowAt(self, x, y):
        self.arrowX = x
        self.arrowY = y

    def resetArrow(self):
        self.arrowX = -50
        self.arrowY = -50

    def draw(self):
        self.TX.render_line_numbers_flag = True
        pygame_events = self.simulation.pygame_events
        if not self.allowWrite:
            pygame_events = [e for e in pygame_events if e.type not in (pygame.KEYDOWN, pygame.KEYUP)]
        self.TX.display_editor(pygame_events, self.simulation.pressed_keys,
                               self.simulation.mouse_x, self.simulation.mouse_y, self.simulation.mouse_pressed)
        
        x = self.offset_x + self.font_size*.5                                                              # Arrow at begining of TX
        y = self.offset_y + self.font_size/2 - self.font_size*1.1*self.TX.first_showable_line_index      # Arrow at begining of TX + moved by scroll
        x += (self.arrowX)* self.TX.letter_width                                                                 # Arrow moved by code
        y += (self.arrowY-1)* self.TX.letter_height*1.1                                                                 # Arrow moved by code

        if self.offset_y <= y <= self.offset_y + self.TX.editor_height:
            pygame.draw.polygon(self.simulation.screen, (255, 0, 0), [
            (x, y),
            (x - 20, y - 10),
            (x - 20, y + 10),])
    def getText(self):
        return self.TX.get_text_as_string()