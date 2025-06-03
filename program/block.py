from typing import Tuple
from . import config

class Block():
    def __init__(self, name: str, value: any, type: str, position: Tuple[int, int], color = config.block_color):
        self.color = color
        self.position = position
        self.name = name
        self.value = value
        self.type = type
        self.x_pos = None
        self.y_pos = None
    
    def highlight(self, color = config.block_heghlight_color):
        self.color = color
    def unhighlight(self):
        self.color = config.block_color
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getType(self):
        return self.type
    def getColor(self):
        return self.color
    def getPosition(self):
        return self.position
    def add(self, value: float):
        self.value += value
    def x(self):
        return self.position[0]
    def y(self):
        return self.position[1]
    
    


