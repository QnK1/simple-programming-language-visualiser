import config
from typing import Tuple

class Block():
    def __init__(self, name: str, value: any, position: Tuple[int, int]):
        
        self.color = config.block_color
        self.position = position
        self.name = name
        self.value = value
    
    def highlight(self, color = config.block_heghlight_color):
        self.color = color
    def unhighlight(self):
        self.color = config.block_color
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
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
    
    


