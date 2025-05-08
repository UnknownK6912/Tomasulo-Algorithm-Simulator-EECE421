class restation:
    def __init__(self):
        self.ALU1Empty = True
        self.ALU1Ready = False
        self.ALU1OP1 = None
        self.ALU1OP2 = None
        self.ALU1OP = None

        self.ALU2Empty = True
        self.ALU2Ready = False
        self.ALU2OP1 = None
        self.ALU2OP2 = None
        self.ALU2OP = None
        
        self.ALU3Empty = True
        self.ALU3Ready = False
        self.ALU3OP1 = None
        self.ALU3OP2 = None
        self.ALU3OP = None
        
        self.MULDIV1Empty = True
        self.MULDIV1Ready = False
        self.MULDIV1OP1 = None
        self.MULDIV1OP2 = None
        self.MULDIV1OP = None
        
        self.MULDIV2Empty = True
        self.MULDIV2Ready = False
        self.MULDIV2OP1 = None
        self.MULDIV2OP2 = None
        self.MULDIV2OP = None
        
        self.LOAD1 = 'empty'
        self.LOAD1Ready = False
        
        self.LOAD2 = 'empty'
        self.LOAD2Ready = False
        
        self.STORE1 = 'empty'
        self.STORE1Ready = False
        
        self.STORE2 = 'empty'
        self.STORE2Ready = False

    def issueMULDIV(self, instruction, registerFile):
        if(self.MULDIV1Empty == True):
            instruction = instruction.split(" ")
            self.MULDIV1Empty = False

            self.MULDIV1OP1 = registerFile.getValue(int(instruction[2][1:-1]))
            self.MULDIV1OP2 = registerFile.getValue(int(instruction[3][1:]))
            registerFile.subscribe(int(instruction[1][1:-1]), "MULDIV1")
            self.MULDIV1OP = instruction[0]
            return True
        elif(self.MULDIV2Empty == True):
            instruction = instruction.split(" ")
            self.MULDIV2Empty = False

            self.MULDIV2OP1 = registerFile.getValue(int(instruction[2][1:-1]))
            self.MULDIV2OP2 = registerFile.getValue(int(instruction[3][1:]))
            registerFile.subscribe(int(instruction[1][1:-1]), "MULDIV2")
            self.MULDIV2OP = instruction[0]
            return True
        else:
            return False

    #instruction format: "ADD R1, R2, R3"
    def issueALU(self, instruction, registerFile):
        if(self.ALU1Empty == True):
            instruction = instruction.split(" ")
            self.ALU1Empty = False

            self.ALU1OP1 = registerFile.getValue(int(instruction[2][1:-1]))
            self.ALU1OP2 = registerFile.getValue(int(instruction[3][1:]))
            registerFile.subscribe(int(instruction[1][1:-1]), "ALU1")
            self.ALU1OP = instruction[0]
            return True
        elif(self.ALU2Empty == True):
            instruction = instruction.split(" ")
            self.ALU2Empty = False

            self.ALU2OP1 = registerFile.getValue(int(instruction[2][1:-1]))
            self.ALU2OP2 = registerFile.getValue(int(instruction[3][1:]))
            registerFile.subscribe(int(instruction[1][1:-1]), "ALU2")
            self.ALU2OP = instruction[0]
            return True
        elif(self.ALU3Empty == True):
            instruction = instruction.split(" ")
            self.ALU3Empty = False

            self.ALU3OP1 = registerFile.getValue(int(instruction[2][1:-1]))
            self.ALU3OP2 = registerFile.getValue(int(instruction[3][1:]))
            registerFile.subscribe(int(instruction[1][1:-1]), "ALU3")
            self.ALU3OP = instruction[0]
            return True
        else:
            return False
    
    
    def refreshALU(self, cdb, ALU1Unit, ALU2Unit, MULDIVUnit):
        if (not self.ALU1Ready) and (self.ALU1Empty != True):
            if type(self.ALU1OP1) == str:
                if cdb[self.ALU1OP1] != None:
                    self.ALU1OP1 = cdb[self.ALU1OP1]
            if type(self.ALU1OP2) == str:
                if cdb[self.ALU1OP2] != None:
                    self.ALU1OP2 = cdb[self.ALU1OP2]
            if type(self.ALU1OP1) == int and type(self.ALU1OP2) == int:
                self.ALU1Ready = True
        elif self.ALU1Ready and not self.ALU1Empty:
            if ALU1Unit.isBusy() == False:
                ALU1Unit.exec(self.ALU1OP1, self.ALU1OP2, self.ALU1OP, "ALU1")
                self.ALU1Ready = False
                self.ALU1OP1 = None
                self.ALU1OP2 = None
                self.ALU1OP = None
                self.ALU1Empty = True
            elif ALU2Unit.isBusy() == False:
                ALU2Unit.exec(self.ALU1OP1, self.ALU1OP2, self.ALU1OP, "ALU1")
                self.ALU1Ready = False
                self.ALU1OP1 = None
                self.ALU1OP2 = None
                self.ALU1OP = None
                self.ALU1Empty = True
        
        if (not self.ALU2Ready) and (self.ALU2Empty != True):
            if type(self.ALU2OP1) == str:
                if cdb[self.ALU2OP1] != None:
                    self.ALU2OP1 = cdb[self.ALU2OP1]
            if type(self.ALU2OP2) == str:
                if cdb[self.ALU2OP2] != None:
                    self.ALU2OP2 = cdb[self.ALU2OP2]
            if type(self.ALU2OP1) == int and type(self.ALU2OP2) == int:
                self.ALU2Ready = True
        elif self.ALU2Ready and not self.ALU2Empty:
            if ALU1Unit.isBusy() == False:
                ALU1Unit.exec(self.ALU2OP1, self.ALU2OP2, self.ALU2OP, "ALU2")
                self.ALU2Ready = False
                self.ALU2OP1 = None
                self.ALU2OP2 = None
                self.ALU2OP = None
                self.ALU2Empty = True
            elif ALU2Unit.isBusy() == False:
                ALU2Unit.exec(self.ALU2OP1, self.ALU2OP2, self.ALU2OP, "ALU2")
                self.ALU2Ready = False
                self.ALU2OP1 = None
                self.ALU2OP2 = None
                self.ALU2OP = None
                self.ALU2Empty = True

        if (not self.ALU3Ready) and (self.ALU3Empty != True):
            if type(self.ALU3OP1) == str:
                if cdb[self.ALU3OP1] != None:
                    self.ALU3OP1 = cdb[self.ALU3OP1]
            if type(self.ALU3OP2) == str:
                if cdb[self.ALU3OP2] != None:
                    self.ALU3OP2 = cdb[self.ALU3OP2]
            if type(self.ALU3OP1) == int and type(self.ALU3OP2) == int:
                self.ALU3Ready = True
        elif self.ALU3Ready and not self.ALU3Empty:
            if ALU1Unit.isBusy() == False:
                ALU1Unit.exec(self.ALU3OP1, self.ALU3OP2, self.ALU3OP, "ALU3")
                self.ALU3Ready = False
                self.ALU3OP1 = None
                self.ALU3OP2 = None
                self.ALU3OP = None
                self.ALU3Empty = True
            elif ALU2Unit.isBusy() == False:
                ALU2Unit.exec(self.ALU3OP1, self.ALU3OP2, self.ALU3OP, "ALU3")
                self.ALU3Ready = False
                self.ALU3OP1 = None
                self.ALU3OP2 = None
                self.ALU3OP = None
                self.ALU3Empty = True

        if (not self.MULDIV1Ready) and (self.MULDIV1Empty != True):
            if type(self.MULDIV1OP1) == str:
                if cdb[self.MULDIV1OP1] != None:
                    self.MULDIV1OP1 = cdb[self.MULDIV1OP1]
            if type(self.MULDIV1OP2) == str:
                if cdb[self.MULDIV1OP2] != None:
                    self.MULDIV1OP2 = cdb[self.MULDIV1OP2]
            if type(self.MULDIV1OP1) == int and type(self.MULDIV1OP2) == int:
                self.MULDIV1Ready = True
        elif self.MULDIV1Ready and not self.MULDIV1Empty:
            if MULDIVUnit.isBusy() == False:
                MULDIVUnit.exec(self.MULDIV1OP1, self.MULDIV1OP2, self.MULDIV1OP, "MULDIV1")
                self.MULDIV1Ready = False
                self.MULDIV1OP1 = None
                self.MULDIV1OP2 = None
                self.MULDIV1OP = None
                self.MULDIV1Empty = True
        
        if (not self.MULDIV2Ready) and (self.MULDIV2Empty != True):
            if type(self.MULDIV2OP1) == str:
                if cdb[self.MULDIV2OP1] != None:
                    self.MULDIV2OP1 = cdb[self.MULDIV2OP1]
            if type(self.MULDIV2OP2) == str:
                if cdb[self.MULDIV2OP2] != None:
                    self.MULDIV2OP2 = cdb[self.MULDIV2OP2]
            if type(self.MULDIV2OP1) == int and type(self.MULDIV2OP2) == int:
                self.MULDIV2Ready = True
        elif self.MULDIV2Ready and not self.MULDIV2Empty:
            if MULDIVUnit.isBusy() == False:
                MULDIVUnit.exec(self.MULDIV2OP1, self.MULDIV2OP2, self.MULDIV2OP, "MULDIV2")
                self.MULDIV2Ready = False
                self.MULDIV2OP1 = None
                self.MULDIV2OP2 = None
                self.MULDIV2OP = None
                self.MULDIV2Empty = True