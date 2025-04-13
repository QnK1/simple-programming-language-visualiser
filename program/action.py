from block import Block

class Action:
    def __init__(self, block : Block, lifeTime : int, endFunction : callable):
        self.block = block
        self.lifeTime = lifeTime
        self.endFunction = endFunction
    def tick(self):
        self.ticks -= 1
        if self.ticks == 0:
            self.endFunction()
    def getLifeTime(self): return self.lifeTime
    