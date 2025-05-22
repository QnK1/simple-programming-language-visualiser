import pygame, sys, os

from pathlib import Path
from collections import deque
from . import config
from .board import Board
from .block import Block
from .visuals import Visuals
from .buttonDisplay import ButtonDisplay
from .showCode import ShowCode
from .myTextEditor import MyTextEditor
from interface.get_pygments_tokens import SyntaxHighlighter

class Simulation:

    def __init__(self):
        # Initialization
        pygame.init()
        info = pygame.display.Info()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
        self.screen = pygame.display.set_mode((info.current_w, info.current_h))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.tps = config.ticks_per_second
        self.boards = []
        self.boards.append(Board(self, 'Main variables', 0))
        self.globals = Board(self, 'Global variables', config.globals_height)
        self.visuals = Visuals(self)
        self.queue = deque()
        self.queueWaitTicks = 0
        self.buttonDisplay = ButtonDisplay(self)
        self.showCode = ShowCode(self)
        self.textEditor = MyTextEditor(self)

        self.visuals.setCurrentCode('l = [1,2,3]', 4, 55)
        self.visuals.setVariable('l', [1,2,3])

        self.visuals.setCurrentCode('s1 = "text"', 5, 56)
        self.visuals.setVariable('s1', "text")

        self.visuals.setCurrentCode('s2 = "longer_text"', 5, 99)
        self.visuals.setVariable('s2', "longer_text")

        self.visuals.setCurrentCode('a = 2', 4, 5)
        self.visuals.setVariable('a', 2)

        self.visuals.setCurrentCode('b = 6', 4, 5)
        self.visuals.setVariable('b', 6)

        self.visuals.setCurrentCode('c = a + b', 4, 55)
        self.visuals.setCurrentCode('c = 2 + b', 4, 5)
        self.visuals.setCurrentCode('c = 2 + 6', 8, 9)
        self.visuals.setCurrentCode('c = 8', 4, 5)
        self.visuals.setVariable('c', 8)

        self.visuals.setCurrentCode('d = multiply_func(a, b)')
        self.visuals.setCurrentCode('d = multiply_func(2, b)', 18, 19)
        self.visuals.setCurrentCode('d = multiply_func(2, 6)', 21, 22)
        self.visuals.setCurrentCode('d = multiply_func(2, 6)')
        self.visuals.openFunction('multiply_func')
        self.visuals.setVariable('a', 2)
        self.visuals.setVariable('b', 6)
        self.visuals.setCurrentCode('return = a * b', 9, 14)
        self.visuals.setCurrentCode('return = 2 * b', 9, 10)
        self.visuals.setCurrentCode('return = 2 * 6', 13, 14)
        self.visuals.setCurrentCode('return = 12', 9, 11)
        self.visuals.closeFunction()
        self.visuals.setCurrentCode('d = multiply_func(a, b)', 4, 99)
        self.visuals.setCurrentCode('d = 12', 4, 99)
        self.visuals.setVariable('d', 12)

        # self.visuals.setCurrentCode('a += 4', 5, 6)
        # self.visuals.add('a', 4)
        # self.visuals.setCurrentCode('a += 6', 5, 6)
        # self.visuals.add('a', 6)
        # self.visuals.openFunction('funkcja')
        # self.visuals.setVariable('a', 2)
        # self.visuals.setVariable('b', 2)
        # self.visuals.add('a', 15)
        # self.visuals.add('a', 'b')
        # self.visuals.closeFunction()

        while True:
            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0            # tps_delta is in seconds
            while self.tps_delta > 1 / self.tps:                  # 1 tick per 1/60 second (if tps_max is 60)
                # Events
                self.pygame_events = pygame.event.get()
                self.pressed_keys = pygame.key.get_pressed()
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                self.mouse_pressed = pygame.mouse.get_pressed()
                self.checkKeys()

                if self.queueWaitTicks <= 0 and len(self.queue):
                    self.queue.popleft()()
                    self.queueWaitTicks = config.action_tick_time + config.action_delay
                self.tick()
                self.queueWaitTicks -= 1
                self.tps_delta -= 1/ self.tps
                
                # Drawing                                               
                self.draw()

    def tick(self):
        self.visuals.tick()

    def draw(self):
        # self.screen.fill((0,0,0))                                 # background color
        self.screen.fill((0, 0, 0), rect=(0, 0, 1000, 1080))        # dont fill text editor, blinking line number bug
        self.boards[-1].draw(self.mouse_x, self.mouse_y)
        self.globals.draw(self.mouse_x, self.mouse_y)
        self.buttonDisplay.draw()
        self.showCode.draw()
        self.textEditor.draw()
        pygame.display.flip()                              # update screen
    def checkKeys(self):
        for event in self.pygame_events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
if __name__ == "__main__":
    Simulation()
