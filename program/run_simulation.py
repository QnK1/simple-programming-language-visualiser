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
from interpreter.main import run
from interpreter.run_utils import *

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
        self.showCode = ShowCode(self)
        self.textEditor = MyTextEditor(self)
        self.buttonDisplay = ButtonDisplay(self)
        self.buttonDisplay.addButton(1000, 1010, 120, 50, 'Run', [lambda: self.executeCode()], blink=True)
        self.buttonDisplay.addButton(1150, 1010, 120, 50, 'Stop', [lambda: self.calcelExecution()], blink=True)
        self.buttonDisplay.addButton(1300, 1010, 120, 50, 'Pause', [lambda: self.pause()])
        self.buttonDisplay.addButton(1000, 930, 420, 50, 'Speed', [], type='slider')
        self.tempx = -50
        self.tempy = -50
        self.paused = False

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
        self.buttonDisplay.tick()
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

    def pause(self):
        if self.paused:
            self.queueWaitTicks = 0
            self.buttonDisplay.buttons['Pause'].button_color = config.button_color
        else:
            self.queueWaitTicks = 10**6
            self.buttonDisplay.buttons['Pause'].button_color = config.button_paused_color
        self.paused = not self.paused

    def handleExpression(self, expression, prefix = ""):
        for stage in expression.stages:
            if isinstance(stage.content, str):
                self.visuals.setCurrentCode(prefix + stage.content, x=self.tempx, y=self.tempy)
            elif isinstance(stage.content, list):
                for statement in stage.content:
                    self.handleStatement(statement)
            # else:
            #     self.visuals.setCurrentCode(prefix + str(stage.content), x=self.tempx, y=self.tempy)
            #     print("TO NIE POWINNO SIE STAĆ? - EXPRESSION, func call -> ", stage.is_function_call)

    def handleStatement(self, statement):

        if isinstance(statement, FunctionDefinitionStatement):
            return
        
        self.tempx, self.tempy = statement.column_start, statement.line_start

        if isinstance(statement, VariableDefinitionStatement):
            self.handleExpression(statement.rhs_exp, statement.name + " = ")
            self.visuals.setCurrentCode(statement.name + " = " + str(statement.final_val), x=self.tempx, y=self.tempy)
            self.visuals.setVariable(statement.name, statement.final_val, statement.type, statement.scope == ScopeType.GLOBAL)

        elif isinstance(statement, VariableAssignmentStatement):
            self.handleExpression(statement.rhs_exp, statement.name + " = ")
            if statement.is_list_indexing:
                for expr in statement.index_exps:
                    self.handleExpression(expr)
                at = "".join(f"[{i}]" for i in statement.final_indices)
                self.visuals.setCurrentCode(statement.name + at + " = " + str(statement.final_val), x=self.tempx, y=self.tempy)
                self.visuals.assignValue(statement.name, statement.final_val, statement.final_indices, statement.scope == ScopeType.GLOBAL)
            else:
                self.visuals.setCurrentCode(statement.name + " = " + str(statement.final_val), x=self.tempx, y=self.tempy)
                self.visuals.setVariable(statement.name, statement.final_val, statement.type, statement.scope == ScopeType.GLOBAL)
                

        elif isinstance(statement, ReturnStatement):
            self.handleExpression(statement.return_exp, prefix='return -> ')
            self.visuals.setCurrentCode('return -> ' + str(statement.return_val), x=self.tempx, y=self.tempy)
            self.visuals.closeFunction()
        
        elif isinstance(statement, FunctionCallStatement):
            for index, pair in enumerate(zip(statement.arg_expressions, statement.arg_values), start=1):
                self.handleExpression(pair[0], prefix=f"arg{index} -> ")
                self.visuals.setCurrentCode(statement.function_name + f" arg{index} -> " + str(pair[1]), x=self.tempx, y=self.tempy)
            self.visuals.openFunction(statement.function_name)
        
        elif isinstance(statement, IfStatement):
            self.handleExpression(statement.condition_exp)
        
        elif isinstance(statement, WhileStatement):
            self.handleExpression(statement.condition_exp)

        elif isinstance(statement, LoopStatement):
            self.handleExpression(statement.iterated_exp)

            
    def calcelExecution(self):
        self.queue.clear()
        self.visuals.actions.clear()
        self.showCode.text = ''
        self.boards = self.boards[0:1]
        self.boards[0].blocks.clear()
        self.globals.blocks.clear()

    def executeCode(self):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print(self.textEditor.getText())
        # for el in run(self.textEditor.getText())[1]:
        #     print(type(el), el)
        value = run(self.textEditor.getText())
        print('############################################')
        print(value[1])
        self.calcelExecution()
        if value[1] == None:
            print('ERRORS!!!!')
            print(value[0])
        else:
            for el in value[1]:
                self.handleStatement(el)
            self.visuals.setCurrentCode('')



if __name__ == "__main__":
    Simulation()
