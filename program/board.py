import pygame, math, random 
from . import config
from .block import Block

class Board():
    def __init__(self, simulation, name: str, top_spacing: int):
        self.simulation = simulation
        self.name = name
        self.top_spacing = top_spacing
        self.width = config.blocks_width                 # rewrite for faster (~50% faster) computations
        self.block_size = config.block_size
        self.block_border_size = config.block_border_size
        self.font_size = config.font_size
        self.title_font_size = config.title_font_size
        self.title_height = config.title_height
        self.border_spacing = config.border_spacing
        self.blocks = {}                                 # Dict[variable_name : Block]
    def setBlock(self, name: str, value: any):
        """Add or change variable name/type/value"""
        self.blocks[name] = Block(name, value, (len(self.blocks)//self.width, len(self.blocks)%self.width))
    def tick(self):
        # self.mover.tick()

        pass

    def draw(self):
        font = pygame.font.Font(None, self.title_font_size)
        title = font.render(self.name, True, (100,100,100))
        self.simulation.screen.blit(title, (self.border_spacing, self.top_spacing + self.border_spacing))
        for var in self.blocks.values():
            cur_height = var.x() * (self.block_size + self.block_border_size) + self.title_height + self.top_spacing
            cur_width = var.y() * (self.block_size + self.block_border_size)
            pygame.draw.rect(self.simulation.screen, var.getColor(), pygame.Rect(cur_width + self.block_border_size, cur_height + self.block_border_size, self.block_size, self.block_size))
            font = pygame.font.Font(None, self.font_size)
            box_value = font.render(str(var.getValue()), True, (100,100,100))
            box_name = font.render(var.getName(), True, (100,100,100))
            self.simulation.screen.blit(box_value, (cur_width + self.block_border_size + 15,cur_height+self.block_size-15))
            self.simulation.screen.blit(box_name, (cur_width + self.block_border_size + 15,cur_height+self.block_size-65))



