from block import Block

class Action:
    def __init__(self, lifeTime : int, endFunctions : list[callable]):
        self.lifeTime = lifeTime
        self.endFunctions = endFunctions

    