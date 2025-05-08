import random
class LS:
    def __init__(self):
        self.clockCycles = 5
        self.ccExec = 0
        self.result = 0
        self.busy = False
        self.operation = None

    def exec(self, operand1, operand2, operation, tag):
        if self.busy:
            return None
        self.operation = operation
        self.ccExec = 0
        self.busy = True
        self.tag = tag
        if self.operation == "load":
            self.result = random.randint(0, 100)

    def getResult(self):
        if self.operation == "load":
            temp = self.result
            self.result = None
            return (temp,self.tag)
        else:
            return None
    
    def increment(self):
        if self.ccExec == self.clockCycles:
            self.busy = False
        self.ccExec += 1
        return self.busy
    
    def isBusy(self):
        return self.busy