import ALU
import LS
import MULDIV
import REGISTER
import STATION

maxCC = 200
ALU1 = ALU.ALU()
ALU2 = ALU.ALU()
LS1 = LS.LS()
MULDIV1 = MULDIV.MULDIV()
registers = REGISTER.registerFile()
resStations = STATION.restation()

cdb = {"ALU1": None, "ALU2": None, "ALU3": None, "LOAD1": None, "LOAD2": None, "MULDIV1": None, "MULDIV2": None}

instruction = "ADD R2, R3, R4"
instruction2 = "SUB R1, R5, R6"
if resStations.issueALU(instruction, registers):
        print("Instruction1 issued to ALU")
if resStations.issueALU(instruction2, registers):
        print("Instruction2 issued to ALU")
if resStations.issueALU("ADD R3, R7, R3", registers):
        print("Instruction3 issued to ALU")
if resStations.issueMULDIV("MUL R1, R4, R5", registers):
        print("Instruction4 issued to MULDIV")

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

    #the same for the rest of the Units.
    #assume all units are done being checked for values
    resStations.refreshALU(cdb, ALU1, ALU2, MULDIV1)
    registers.refresh(cdb)

print(registers.registers)
print(cdb)