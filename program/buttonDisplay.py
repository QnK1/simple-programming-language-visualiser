import pygame
from . import config
from .button import Button

class ButtonDisplay():
    def __init__(self, simulation):
        self.simulation = simulation
        self.font_size = config.button_font_size
        self.width = config.button_width
        self.height = config.button_height
        self.text_color = config.button_text_color
        self.text_offset_x = config.button_text_offset_x
        self.text_offset_y = config.button_text_offset_y
        self.buttons = {}
        self.prev_mouse_state = False
        self.leftClickX = None
        self.leftClickY = None
        self.leftClick = False
        

    def addButton(self, offset_x: int, offset_y: int, width: int, height: int, text: str, function, blink = False, type = 'button'):
        self.buttons[text]=Button(self.simulation, offset_x, offset_y, width, height, text, function, blink, type)

    def draw(self):
        for button in self.buttons.values():
            pygame.draw.rect(self.simulation.screen, button.button_color, (button.getX(), button.getY(), button.getWidth(), button.getHeight()))
            font = pygame.font.Font(None, self.font_size)
            text = font.render(button.getText(), True, self.text_color)
            self.simulation.screen.blit(text, (button.getX() + self.text_offset_x, button.getY() + self.text_offset_y))
            button.draw()
    
    def tick(self):
        for button in self.buttons.values():
            if button.change_color_delay > 0:
                button.change_color_delay -= 1
            elif button.change_color_delay == 0:
                button.button_color = config.button_color
                button.change_color_delay = -1
                
        leftUnclickX = None
        leftUnclickY = None

        
        
        if self.leftClick:
            for event in self.simulation.pygame_events:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    leftUnclickX = event.pos[0]
                    leftUnclickY = event.pos[1]
                    self.leftClick = False
        else:
            for event in self.simulation.pygame_events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.leftClickX = event.pos[0]
                    self.leftClickY = event.pos[1]
                    self.leftClick = True
        
        if None in [leftUnclickX, leftUnclickY]:
            return

        for button in self.buttons.values():
            if (button.getX() <= leftUnclickX <= button.getX() + button.getWidth() and
                button.getY() <= leftUnclickY <= button.getY() + button.getHeight() and
                button.getX() <= self.leftClickX <= button.getX() + button.getWidth() and
                button.getY() <= self.leftClickY <= button.getY() + button.getHeight()):
                if button.blink:
                    button.button_color = config.button_pressed_color
                    button.change_color_delay = config.button_pressed_color_ticks
                button.executeFunctions()
                button.clicked(leftUnclickX, leftUnclickY)
                break