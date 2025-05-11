import random

try:
    num_instr = int(input("How many instructions do you want to generate?: "))
    assert num_instr > 0, "Number of instructions must be positive"
except ValueError:
    print("Error: Input must be a valid number")
    exit(1)
except AssertionError as e:
    print(f"Error: {e}")
    exit(1)

output_file = open("InstructionLog.txt", "w") # create a file where instructions will be written


num_reg = 8 # number of registers
instr_types = ["ADD", "SUB", "MUL", "DIV", "LOAD", "STORE"] # instruction types
instr_probs = [0.225, 0.225, 0.15, 0.10, 0.18, 0.12] # probabilities for each instruction, indexed to match the instr_type array indices


def gen_instr(num_instr): # function to generate instructions and write them to an output file

    for i in range(0, num_instr):
    
        instr_choice = random.choices(instr_types, weights=instr_probs, k=1)[0] # choose an instruction type based on probabilities defined above

        if instr_choice in ["ADD", "SUB", "MUL", "DIV"]: # format <OP> <DEST>, <SRC1>, <SRC2> for add, sub, mul and div
            instr_line = str(instr_choice) + " R" + str(random.randint(0,num_reg-1)) + ", R" + str(random.randint(0,num_reg-1)) + ", R" + str(random.randint(0,num_reg-1)) + "\n"
    
        elif instr_choice == "LOAD": # format <OP> <DEST>, <OFFSET>(<BASE>) for load
            instr_line = str(instr_choice) + " R" + str(random.randint(0,num_reg-1)) + ", " + str(random.randint(0,1000)) + "(R" + str(random.randint(0,num_reg-1)) + ")"+ "\n"
    
        elif instr_choice == "STORE": # format <OP> <OFFSET>(<BASE>), <SRC>
            instr_line = str(instr_choice) + " " + str(random.randint(0,1000)) + "(R" + str(random.randint(0,num_reg-1)) + ")" + ", R" + str(random.randint(0,num_reg-1)) + "\n"

        output_file.write(instr_line) # written to output file, to be re-read later by the main program


gen_instr(num_instr)
output_file.close()
