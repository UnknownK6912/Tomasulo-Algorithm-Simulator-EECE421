class MULDIV:
    def __init__(self):
        self.clockCyclesMul = 10
        self.clockCyclesDiv = 20
        self.ccExec = 0
        self.result = 0
        self.busy = False
        self.operation = None
        self.tag = None

    def exec(self, operand1, operand2, operation, tag):
        if self.busy:
            return None
        self.operation = operation
        self.ccExec = 0
        self.busy = True
        self.tag = tag
        if operation == "MUL":
            self.result = operand1 * operand2
        elif operation == "DIV":
            self.result = operand1 / operand2

    def getResult(self):
        if self.operation == "MUL":
            temp = self.result
            self.result = None
            self.operation = None
            return (temp,self.tag)
        elif self.operation == "DIV":
            temp = self.result
            self.result = None
            self.operation = None
            return (temp,self.tag)
        else:
            return (None, None)
    
    def increment(self):
        if self.busy:
            self.ccExec += 1
            if self.operation == "MUL":
                if self.ccExec == self.clockCyclesMul:
                    self.busy = False
            elif self.operation == "DIV":
                if self.ccExec == self.clockCyclesDiv:
                    self.busy = False
        return self.busy
    
    def isBusy(self):
        return self.busy