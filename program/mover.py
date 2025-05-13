from .block import Block
from typing import Tuple

class BlockNotOnBoard(Exception):
    pass

class Mover():
    def __init__(self, board):
        self.transits = []                # list of dicts -> { block : Block, goal :(int, int), tick_step: (int, int), remaining_ticks: int }
        self.board = board

    def tick(self):
        
        for transit in self.transits:
            if transit['remaining_ticks'] == 0:
                transit['block'].unhighlight()
                
        self.transits = [transit for transit in self.transits if transit['remaining_ticks'] != 0]
        for transit in self.transits:
            transit['block'].x_pos += transit['tick_step'][0]
            transit['block'].y_pos += transit['tick_step'][1]
            transit['remaining_ticks'] += 1

    def move(self, block : Block, goal : Tuple[int, int]):
        pass
                

    