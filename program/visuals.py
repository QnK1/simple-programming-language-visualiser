import operator
from .action import Action
from .board import Board
from . import config

class Visuals():
    ops = {
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge
    }
    def __init__(self, simulation):
        self.simulation = simulation
        self.actions = set()                                    # Set[Action] -> Action[block, lifeTime, endFunction]

    def ifFunc(self, var1, logic, var2, result = None):
        blocks = self.simulation.boards[-1].blocks | self.simulation.globals.blocks
        result = self.ops[logic](blocks[var1].getValue(), blocks[var2].getValue())
        color = (0, 255, 0) if result == True else (255, 0, 0)
        blocks[var1].highlight(color)
        blocks[var2].highlight(color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var1].unhighlight(), lambda: blocks[var2].unhighlight()]))

    def setVariable(self, var_name: str, value: float, if_global: bool = False):        # DODAĆ KOD JEŚLI JUZ ZMIENNA ISTNIEJE
        board = self.simulation.globals if if_global == True else self.simulation.boards[-1]
        if board.blocks.contains(var_name):
            board.blocks[var_name].value = value
            return
        board.setBlock(var_name, value)
        board.blocks[var_name].highlight(config.change_color)
        self.actions.add(Action(config.action_tick_time, [lambda: board.blocks[var_name].unhighlight()]))
    
    def add(self, var_name: str, value):
        blocks = self.simulation.boards[-1].blocks | self.simulation.globals.blocks
        add = value if type(value) != str else blocks[value].getValue()
        blocks[var_name].value += add
        blocks[var_name].highlight(config.add_color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var_name].unhighlight()]))

    def multiply(self, var_name: str, value):
        blocks = self.simulation.boards[-1].blocks | self.simulation.globals.blocks
        mul = value if type(value) != str else blocks[value].getValue()
        blocks[var_name].value *= mul
        blocks[var_name].highlight(config.mul_color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var_name].unhighlight()]))

    def divide(self, var_name: str, value):
        blocks = self.simulation.boards[-1].blocks | self.simulation.globals.blocks
        div = value if type(value) != str else blocks[value].getValue()
        blocks[var_name].value /= div
        blocks[var_name].highlight(config.div_color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var_name].unhighlight()]))

    def openFunction(self, name):
        self.simulation.boards.append(Board(self.simulation, name, 0))

    def closeFunction(self):
        if len(self.simulation.boards) > 1:
            self.simulation.boards.pop()

    def setCurrentCode(self, text, begin, end):
        self.simulation.showCode.text = text
        self.simulation.showCode.begin = begin
        self.simulation.showCode.end = end

    def tick(self):
        delActions = set()
        for action in self.actions:
            action.lifeTime -= 1
            if action.lifeTime <= 0:
                for func in action.endFunctions:
                    func()
                delActions.add(action)
        for action in delActions:
            self.actions.remove(action)


    