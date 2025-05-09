import ALU
import LS
import MULDIV
import REGISTER
import STATION

maxCC = 50
ALU1 = ALU.ALU()
ALU2 = ALU.ALU()
LS1 = LS.LS()
MULDIV1 = MULDIV.MULDIV()
registers = REGISTER.registerFile()
resStations = STATION.restation()

cdb = {"ALU1": None, "ALU2": None, "ALU3": None, "LOAD1": None, "LOAD2": None, "MULDIV1": None, "MULDIV2": None}

if resStations.issueSTORE("STORE 0(R1), R2", registers):
    print("STORE issued")

for cc in range(1, maxCC):
    if(ALU1.increment() == False):
        result = ALU1.getResult()
        if(result[0] != None):
            cdb[result[1]] = result[0]
    
    if(ALU2.increment() == False):
        result = ALU2.getResult()
        if(result[0] != None):
            cdb[result[1]] = result[0]

    if(MULDIV1.increment() == False):
        result = MULDIV1.getResult()
        if(result[0] != None):
            cdb[result[1]] = result[0]
    
    if(LS1.increment() == False):
        result = LS1.getResult()
        if(result[0] != None):
            cdb[result[1]] = result[0]

    #the same for the rest of the Units.
    #assume all units are done being checked for values
    resStations.refreshUnits(cdb, ALU1, ALU2, MULDIV1, LS1)
    registers.refresh(cdb)

print(registers.registers)
print(cdb)