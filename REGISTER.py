class registerFile:
    def __init__(self):
        self.registers = [10, 20, 30, 40, 50, 60, 70, 80]
        self.subscription = [None, None, None, None, None, None, None, None]
        #subscription format is "station name + station number". example: "ALU2"

    def getValue(self, regNum):
        if self.subscription[regNum] == None:
            return self.registers[regNum]
        else:
            return self.subscription[regNum]
    
    #cdb format: {"ALU1": value, "ALU2": value, ALU3: value, "LOAD1": value, "LOAD2": value, "MULDIV1": value, "MULDIV2": value}
    #default value is None
    def refresh(self, cdb):
        for i in range(len(self.subscription)):
            if self.subscription[i] != None:
                if cdb[self.subscription[i]] != None:
                    self.registers[i] = cdb[self.subscription[i]]
                    self.subscription[i] = None
    
    def subscribe(self, regNum, stationName):
        self.subscription[regNum] = stationName