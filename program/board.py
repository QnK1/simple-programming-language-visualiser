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
        self.block_spacing = config.block_spacing
        self.board_offset = config.board_offset
        self.block_text_color = config.block_text_color
        self.font_size = config.font_size
        self.title_color = config.title_color
        self.title_font_size = config.title_font_size
        self.title_height = config.title_height
        self.char_limit = config.block_char_limit
        self.hover_color = config.hover_color
        self.hover_text_color = config.hover_text_color
        self.hover_font_size = config.hover_font_size
        self.hover_height = config.hover_height
        self.hover_border_size = config.hover_border_size

        self.blocks = {}                                 # Dict[variable_name : Block]
    def setBlock(self, name: str, value: any, type: str):
        """Add or change variable name/type/value"""
        self.blocks[name] = Block(name, value, type, (len(self.blocks)//self.width, len(self.blocks)%self.width))
        self.blocks[name].x_pos = self.board_offset + self.blocks[name].y()*(self.block_size + self.block_spacing)
        self.blocks[name].y_pos = self.top_spacing + self.title_height + self.board_offset + self.blocks[name].x()*(self.block_size + self.block_spacing)
    def crop(self, value, string_handle = 1, char_limit = config.block_char_limit):
        strValue = str(value)
        if type(value) == str and string_handle:
            strValue = "\"" + strValue + "\""
        if len(str(value)) > char_limit:
            strValue = strValue[:self.char_limit] + ".."  
        return strValue

    def draw(self, mouse_x, mouse_y):
        font = pygame.font.Font(None, self.title_font_size)
        title = font.render(self.name, True, self.title_color)
        self.simulation.screen.blit(title, (self.board_offset, self.top_spacing + self.board_offset))
        for block in self.blocks.values():
            cur_height = block.x() * (self.block_size + self.block_spacing) + self.title_height + self.top_spacing + self.board_offset
            cur_width = block.y() * (self.block_size + self.block_spacing) + self.board_offset
            rect = pygame.Rect(cur_width, cur_height, self.block_size, self.block_size)
            pygame.draw.rect(self.simulation.screen, block.getColor(), rect)
            font = pygame.font.Font(None, self.font_size)                    

            name = font.render(self.crop(block.getName(), 0), True, self.block_text_color)
            value = font.render(self.crop(block.getValue()), True, self.block_text_color)
            
            self.simulation.screen.blit(name, (cur_width + .1 * self.block_size, cur_height + .1 * self.block_size))
            self.simulation.screen.blit(value, (cur_width + .1 * self.block_size, cur_height + .6 * self.block_size))
            
        for block in self.blocks.values():
            if block.x_pos <= mouse_x <= block.x_pos + self.block_size and  block.y_pos <= mouse_y <= block.y_pos + self.block_size:
                name = font.render(block.getName(), True, self.block_text_color)
                value = font.render(self.crop(block.getValue(), 1, 99999), True, self.block_text_color)
                type = font.render(block.getType(), True, self.block_text_color)
                height = self.hover_height
                width = max(.2 * self.block_size + max(name.get_width(), value.get_width(), type.get_width()), self.block_size)
                
                rect = pygame.draw.rect(self.simulation.screen, self.hover_color, (block.x_pos, block.y_pos, width, height)) 
                self.simulation.screen.blit(name, (block.x_pos + .1 * self.block_size, block.y_pos + .1 * self.block_size))
                self.simulation.screen.blit(value, (block.x_pos + .1 * self.block_size, block.y_pos + .6 * self.block_size))
                self.simulation.screen.blit(type, (block.x_pos + .1 * self.block_size, block.y_pos + 1.1 * self.block_size))

