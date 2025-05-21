from pathlib import Path
from . import config
from pygame_texteditor import TextEditor
from interface.get_pygments_tokens import SyntaxHighlighter

class MyTextEditor:
    def __init__(self, simulation):
        self.simulation = simulation
        self.TX = TextEditor(offset_x=config.editor_offset_x, offset_y=config.editor_offset_y, editor_width=config.editor_width,
                                editor_height=config.editor_height, screen=self.simulation.screen)
        self.TX.set_line_numbers(True)
        self.TX.lexer = SyntaxHighlighter()
        self.TX.set_syntax_highlighting(True)
        self.TX.set_colorscheme_from_yaml(Path(__file__).resolve().parent / Path("colors.yaml"))
        self.TX.set_font_size(config.editor_font_size)

    def draw(self):
        self.TX.display_editor(self.simulation.pygame_events, self.simulation.pressed_keys,
                               self.simulation.mouse_x, self.simulation.mouse_y, self.simulation.mouse_pressed)