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

    def ifFunc_q(self, var1, logic, var2, result = None):
        blocks = self.simulation.globals.blocks | self.simulation.boards[-1].blocks
        result = self.ops[logic](blocks[var1].getValue(), blocks[var2].getValue())
        color = (0, 255, 0) if result == True else (255, 0, 0)
        blocks[var1].highlight(color)
        blocks[var2].highlight(color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var1].unhighlight(), lambda: blocks[var2].unhighlight()]))

    def setVariable_q(self, var_name: str, value: float, type: str, if_global: bool = False):        # DODAĆ KOD JEŚLI JUZ ZMIENNA ISTNIEJE
        board = self.simulation.globals if if_global == True else self.simulation.boards[-1]
        if var_name in board.blocks.keys():
            board.blocks[var_name].value = value
            board.blocks[var_name].type = type
        else:
            board.setBlock(var_name, value, type)
        board.blocks[var_name].highlight(config.change_color)
        self.actions.add(Action(config.action_tick_time, [lambda: board.blocks[var_name].unhighlight()]))
    
    def add_q(self, var_name: str, value):
        blocks = self.simulation.globals.blocks | self.simulation.boards[-1].blocks
        add = value if type(value) != str else blocks[value].getValue()
        blocks[var_name].value += add
        blocks[var_name].highlight(config.add_color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var_name].unhighlight()]))

    def multiply_q(self, var_name: str, value):
        blocks = self.simulation.globals.blocks | self.simulation.boards[-1].blocks
        mul = value if type(value) != str else blocks[value].getValue()
        blocks[var_name].value *= mul
        blocks[var_name].highlight(config.mul_color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var_name].unhighlight()]))

    def divide_q(self, var_name: str, value):
        blocks = self.simulation.globals.blocks | self.simulation.boards[-1].blocks
        div = value if type(value) != str else blocks[value].getValue()
        blocks[var_name].value /= div
        blocks[var_name].highlight(config.div_color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var_name].unhighlight()]))

    def openFunction_q(self, name, x, y):
        self.simulation.boards.append(Board(self.simulation, name, 0))
        self.simulation.textEditor.arrowAt(x, y)

    def closeFunction_q(self):
        if len(self.simulation.boards) > 1:
            self.simulation.boards.pop()

    def setCurrentCode_q(self, text, begin=0, end=0, x=-50, y=-50):
        self.simulation.showCode.text = text
        self.simulation.showCode.begin = begin
        self.simulation.showCode.end = end
        self.simulation.textEditor.arrowAt(x, y)

    def assignValue_q(self, name, value, index_exps, if_global):
        blocks = self.simulation.globals.blocks if if_global else self.simulation.boards[-1].blocks
        current = blocks[name].value
        for idx in index_exps[:-1]:
            current = current[idx]
        current[index_exps[-1]] = value
        blocks[name].highlight(config.change_color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[name].unhighlight()]))

    def ifFunc(self, var1, logic, var2, result = None):
        self.simulation.queue.append(lambda: self.ifFunc_q(var1, logic, var2, result))

    def setVariable(self, var_name: str, value: float, type: str, if_global: bool = False):
        self.simulation.queue.append(lambda: self.setVariable_q(var_name, value, type, if_global))

    def add(self, var_name: str, value):
        self.simulation.queue.append(lambda: self.add_q(var_name, value))

    def multiply(self, var_name: str, value):
        self.simulation.queue.append(lambda: self.multiply_q(var_name, value))

    def divide(self, var_name: str, value):
        self.simulation.queue.append(lambda: self.divide_q(var_name, value))

    def openFunction(self, name, x, y):
        self.simulation.queue.append(lambda: self.openFunction_q(name, x, y))

    def closeFunction(self):
        self.simulation.queue.append(lambda: self.closeFunction_q())

    def setCurrentCode(self, text, begin = 0, end = 0, x=-50, y=-50):
        self.simulation.queue.append(lambda: self.setCurrentCode_q(text, begin, end, x, y))

    def assignValue(self, name, value, index_exps, if_global: bool = False):
        self.simulation.queue.append(lambda: self.assignValue_q(name, value, index_exps, if_global))

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


    