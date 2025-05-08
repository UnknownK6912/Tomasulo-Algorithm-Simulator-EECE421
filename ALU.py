class ALU:
    def __init__(self):
        self.clockCycles = 2
        self.ccExec = 0
        self.result = None
        self.busy = False
        self.tag = None

    def exec(self, operand1, operand2, operation, tag):
        if self.busy:
            return None
        self.ccExec = 0
        self.busy = True
        self.tag = tag
        if operation == "SUB":
            operand2 = -operand2
        self.result = operand1 + operand2
    
    def getResult(self):
        temp = self.result
        self.result = None
        return (temp, self.tag)
        
    def increment(self):
        if self.busy:
            self.ccExec += 1
            if self.ccExec == self.clockCycles:
                self.busy = False
        return self.busy
    
    def isBusy(self):
        return self.busy