import operator
from action import Action
import config

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

    def if_func(self, var1, logic, var2):
        boards = self.simulation.boards[-1] | self.simulation.globals
        result = self.ops[logic](boards[var1].getValue(), boards[var2].getValue())
        print('result ' + str(type(result)) + '    -> ', result)
        color = (0, 255, 0) if result == 1 else (255, 0, 0)
        blocks = self.simulation.boards[-1].blocks | self.simulation.globals.blocks
        blocks[var1].highlight(color)
        blocks[var2].highlight(color)
        self.actions.add(Action(config.action_tick_time, [lambda: blocks[var1].unhighlight(), lambda: blocks[var2].unhighlight()]))

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


    