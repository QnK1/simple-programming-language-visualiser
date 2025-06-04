from . import config
import pygame

class Button():
    def __init__(self, simulation, x: int, y: int, width: int, height: int, text: str, functions: list, blink: bool, type: str):
        self.simulation = simulation
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.functions = functions
        self.button_color = config.button_color
        self.change_color_delay = -1
        self.blink = blink
        self.type = type
        self.last_mouse_click_x = width/2

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def getText(self):
        return self.text
    
    def getSliderValue(self):
        value = max(min(.9, self.last_mouse_click_x/(max(self.width,1))), .1) + .5

        if value > 1.3:
            value = value + (value-1) * 10

        elif value > 1:
            value = value + (value-1) * 3
        return value

    def executeFunctions(self):
        for func in self.functions:
            func()

    def clicked(self, x, y = None):
        self.last_mouse_click_x = max(min(x-self.x, self.width-25),25)
        
    def draw(self):
        if self.type == 'slider':
            pygame.draw.rect(self.simulation.screen, (255,255,255), pygame.Rect(self.last_mouse_click_x-10 + self.x, self.y+self.height/2-10, 20, 20))