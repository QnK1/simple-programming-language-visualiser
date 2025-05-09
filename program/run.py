import pygame, sys, os
import pygame_gui
import config, queue, time
from board import Board
from block import Block
from visuals import Visuals
from codeDisplay import CodeDisplay
from showCode import ShowCode
class Simulation:

    def __init__(self):
        # Initialization
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
        self.screen = pygame.display.set_mode(config.fullscreen_screen_size)
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.tps = config.ticks_per_second
        self.boards = []
        self.boards.append(Board(self, 'Main variables', 0))
        self.globals = Board(self, 'Global variables', config.globals_height)
        self.visuals = Visuals(self)
        self.queue = []
        self.queueWaitTicks = 0
        self.codeDisplay = CodeDisplay(self)
        self.showCode = ShowCode(self)

        self.queue.append(lambda: self.visuals.setCurrentCode('a += 2', 5, 6))
        self.queue.append(lambda: self.visuals.setCurrentCode('a += 4', 5, 6))
        self.queue.append(lambda: self.visuals.setCurrentCode('a += 6', 5, 6))
        self.queue.append(lambda: self.visuals.setVariable('a', 2))
        self.queue.append(lambda: self.visuals.setVariable('b', 3))
        self.queue.append(lambda: self.visuals.add('a', 15))
        self.queue.append(lambda: self.visuals.add('a', 'b'))
        self.queue.append(lambda: self.visuals.multiply('a', 2))
        self.queue.append(lambda: self.visuals.multiply('a', 'b'))
        self.queue.append(lambda: self.visuals.divide('a', 'b'))
        self.queue.append(lambda: self.visuals.divide('a', 2))
        self.queue.append(lambda: self.visuals.ifFunc('a', '==', 'b'))
        self.queue.append(lambda: self.visuals.setVariable('c', 3, True))
        self.queue.append(lambda: self.visuals.openFunction('funkcja'))
        self.queue.append(lambda: self.visuals.setVariable('a', 2))
        self.queue.append(lambda: self.visuals.setVariable('b', 3))
        self.queue.append(lambda: self.visuals.add('a', 15))
        self.queue.append(lambda: self.visuals.add('a', 'b'))
        self.queue.append(lambda: self.visuals.multiply('a', 2))
        self.queue.append(lambda: self.visuals.multiply('a', 'b'))
        self.queue.append(lambda: self.visuals.closeFunction())
        self.queue.append(lambda: self.visuals.add('a', 15))
        self.queue.append(lambda: self.visuals.add('a', 'b'))
        self.queue.append(lambda: self.visuals.multiply('a', 2))
        self.queue.append(lambda: self.visuals.multiply('a', 'b'))
        

        while True:

            # Events
            self.checkEvents()

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0            # tps_delta is in seconds
            while self.tps_delta > 1 / self.tps:                  # 1 tick per 1/60 second (if tps_max is 60)
                if self.queueWaitTicks <= 0 and len(self.queue):
                    self.queue.pop(0)()
                    self.queueWaitTicks = config.action_tick_time + config.action_delay
                self.tick()
                self.queueWaitTicks -= 1
                self.tps_delta -= 1/ self.tps

            # Drawing                                               
            self.draw()

    def tick(self):
        self.boards[-1].tick()
        self.visuals.tick()

    def draw(self):
        self.screen.fill((0,0,0))                               # background color
        self.boards[-1].draw()
        self.globals.draw()
        self.codeDisplay.draw()
        self.showCode.draw()
        pygame.display.flip()                                   # update screen
    def checkEvents(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
if __name__ == "__main__":
    Simulation()
