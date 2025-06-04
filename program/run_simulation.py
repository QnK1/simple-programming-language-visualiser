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
from .errorDisplay import ErrorDisplay

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
        self.boards.append(Board(self, '', 0))
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
        self.function_args = {}
        self.errorDisplay = ErrorDisplay(self)

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
                    to_execute = self.queue.popleft()
                    if isinstance(to_execute, list):
                        for el in to_execute:
                            el()
                    else:
                        to_execute()
                    self.queueWaitTicks = (config.action_delay + config.action_tick_time) /self.buttonDisplay.buttons['Speed'].getSliderValue()
                self.tick()
                self.queueWaitTicks -= 1
                self.tps_delta -= 1/ self.tps
                
                # Drawing                                               
                self.draw()

    def tick(self):
        self.buttonDisplay.tick()
        self.visuals.tick()
    def draw(self):
        self.screen.fill((0,0,0))                                 # background color
        # self.screen.fill((0, 0, 0), rect=(0, 0, 1000, 1080))        # dont fill text editor, blinking line number bug
        self.boards[-1].draw(self.mouse_x, self.mouse_y)
        self.globals.draw(self.mouse_x, self.mouse_y)
        self.buttonDisplay.draw()
        self.showCode.draw()
        self.textEditor.draw()
        self.errorDisplay.draw()
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

    class FunctionParams:
        def __init__(self, args, x, y):
            self.args = args
            self.x = x
            self.y = y

    def handleExpression(self, expression, prefix = "", x=None, y=None):
        if x is None or y is None:
            x, y = self.tempx, self.tempy
        if expression == None:
            return 
        for stage in expression.stages:
            if isinstance(stage.content, str):
                self.visuals.setCurrentCode(prefix + stage.content, x=x, y=y)
            elif isinstance(stage.content, list):
                for statement in stage.content:
                    self.handleStatement(statement)

    def handleStatement(self, statement):
        self.tempx, self.tempy = statement.column_start, statement.line_start

        if isinstance(statement, FunctionDefinitionStatement):
            self.function_args[statement.name] = self.FunctionParams(statement.args, self.tempx, self.tempy)
        
        elif isinstance(statement, VariableDefinitionStatement):
            cur_x, cur_y = self.tempx, self.tempy
            self.handleExpression(statement.rhs_exp, statement.name + " = ")
            self.visuals.setCurrentCode(statement.name + " = " + str(statement.final_val), x=cur_x, y=cur_y)
            self.visuals.setVariable(statement.name, statement.final_val, statement.type, statement.scope == ScopeType.GLOBAL)

        elif isinstance(statement, VariableAssignmentStatement):
            cur_x, cur_y = self.tempx, self.tempy
            self.handleExpression(statement.rhs_exp, statement.name + " = ")
            if statement.is_list_indexing:
                for expr in statement.index_exps:
                    self.handleExpression(expr)
                at = "".join(f"[{i}]" for i in statement.final_indices)
                self.visuals.setCurrentCode(statement.name + at + " = " + str(statement.final_val), x=cur_x, y=cur_y)
                self.visuals.assignValue(statement.name, statement.final_val, statement.final_indices, statement.scope == ScopeType.GLOBAL)
            else:
                self.visuals.setCurrentCode(statement.name + " = " + str(statement.final_val), x=cur_x, y=cur_y)
                self.visuals.setVariable(statement.name, statement.final_val, statement.type, statement.scope == ScopeType.GLOBAL)
                

        elif isinstance(statement, ReturnStatement):
            cur_x, cur_y = self.tempx, self.tempy
            self.handleExpression(statement.return_exp, prefix='return -> ', x=cur_x, y=cur_y)
            self.visuals.setCurrentCode('return -> ' + str(statement.return_val), x=cur_x, y=cur_y)
            self.visuals.closeFunction()
        
        elif isinstance(statement, FunctionCallStatement):
            self.visuals.openFunction(statement.function_name+"(" + ", ".join(str(v) for v in statement.arg_values) + ")", self.function_args[statement.function_name].x, self.function_args[statement.function_name].y)
            for index, arg in enumerate(self.function_args[statement.function_name].args):
                self.visuals.setVariable(arg.name, statement.arg_values[index], arg.type, False)
        
        elif isinstance(statement, IfStatement):
            cur_x, cur_y = self.tempx, self.tempy
            self.handleExpression(statement.condition_exp)
            self.visuals.setCurrentCode(str(statement.final_cond_val), x=cur_x, y=cur_y)
        
        elif isinstance(statement, WhileStatement):
            cur_x, cur_y = self.tempx, self.tempy
            self.handleExpression(statement.condition_exp)
            self.visuals.setCurrentCode(str(statement.final_cond_val), x=cur_x, y=cur_y)

        elif isinstance(statement, LoopStatement):
            cur_x, cur_y = self.tempx, self.tempy
            self.visuals.setCurrentCode(str(statement.iterator_name)+' = '+str(statement.iterated_exp_final_val[statement.current_iterator_index]), x=cur_x, y=cur_y)

        elif isinstance(statement, Error):
            queue_list = []
            queue_list.append(lambda: self.errorDisplay.displayErrors([statement.message+' (line='+str(statement.line_start)+', column='+str(statement.column_start)+')']))
            queue_list.append(lambda: self.visuals.setCurrentCode_q('', x=self.tempx, y=self.tempy))
            self.queue.append(queue_list)

  
    def calcelExecution(self):
        self.textEditor.resetArrow()
        self.textEditor.allowWrite = True
        self.queue.clear()
        self.visuals.actions.clear()
        self.showCode.text = ''
        self.boards = self.boards[0:1]
        self.boards[0].blocks.clear()
        self.globals.blocks.clear()
        self.errorDisplay.clearErrors()

    def executeCode(self):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print(self.textEditor.getText())
        # for el in run(self.textEditor.getText())[1]:
        #     print(type(el), el)
        value = run(self.textEditor.getText())
        print('############################################')
        print('Errors:')
        print(value[0])
        print('Statements:')
        print(value[1])
        self.calcelExecution()
        
        if value[1] == None:
            self.errorDisplay.displayErrors(value[0])
        else:
            self.textEditor.allowWrite = False
            for el in value[1]:
                self.handleStatement(el)
            self.queue.append([lambda: self.textEditor.allowWriting(), lambda: self.textEditor.resetArrow()])



if __name__ == "__main__":
    Simulation()
