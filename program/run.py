import pygame, sys, os
import config, queue, time
from board import Board
from block import Block

class Simulation:

    def __init__(self):
        # Initialization
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
        self.screen = pygame.display.set_mode(config.fullscreen_screen_size)
        # fullscreen = False
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.boards = []
        self.boards.append(Board(self, 'Main variables', 0))
        self.boards[0].setBlock('a', 'int', 1)
        self.boards[0].setBlock('b', 'int', 2)
        self.functions = Board(self, 'Functions', 450)
        self.functions.setBlock('add', 'function', '')
        self.globals = Board(self, 'Global variables', 650)
        self.globals.setBlock('c', 'int', 3)
        self.tps = config.ticks_per_second
        self.queue = queue.Queue()
        self.wait = False
        # Events

        self.draw()                         # draw once for buttons/text to spawn
        while True:
            self.checkEvents()
            while self.wait:
                self.checkEvents()
                time.sleep(.1)
            
            while not self.queue.empty:
                
                # Ticking
                self.tps_delta += self.tps_clock.tick() / 1000.0            # tps_delta is in seconds
                while self.tps_delta > 1 / self.tps:                  # 1 tick per 1/60 second (if tps_max is 60)
                    self.tick()
                    self.tps_delta -= 1/ self.tps

                # Drawing                                               
                self.draw()

    def tick(self):
        self.boards[-1].tick()

    def draw(self):
        self.screen.fill((0,0,0))                               # background color
        self.boards[-1].draw()
        self.functions.draw()
        self.globals.draw()
        font = pygame.font.SysFont(None, 36)
        button_rect = pygame.Rect(150, 120, 100, 50)
        button_text = font.render("Kliknij", True, (0,0,0))
        pygame.draw.rect(self.screen, (0,0,155), button_rect)
        self.screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
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
