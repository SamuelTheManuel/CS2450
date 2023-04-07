from UVSim_Calculations import UVSim_Calculations
from UVSimGUI import UVSimGUI

class UVSim():
    def __init__(self, test_bool=False, ):
        # dict entries are like: register_number(string): [DataBool(bool), contents(string)]. DataBool indicates whether
        # the contents are a value or not. if it is false, the contents are an instruction. if it is true, the contents
        # should be ignored.
        self.test_bool = test_bool
        self.memory_dict = {}
        self.accumulator = [False, "000000"]
        self.instruction_amount = 0
        self.Calc = UVSim_Calculations(self)
        self.GUI = UVSimGUI(self, self.test_bool)
        self.initialize_memory()
        if(test_bool is False):
            self.GUI.our_window.mainloop()

    def initialize_memory(self):
        if self.test_bool is False:
            self.GUI.insert_output("Initializing Memory...")
        for i in range(250):  # initiallizes our co
            our_key = i
            if i <= 9:
                our_key = "00" + str(our_key)
            elif i >9 and i<100:
                our_key = "0" + str(our_key)
            else:
                our_key = str(our_key)
            self.memory_dict[our_key] = [True, "000000"]
        if self.test_bool is False:
            self.GUI.insert_output("Memory Set!")


    def initiate_process(self, input_text):
        # loads each instruction into the corresponding register
        for item in range(len(input_text)):
            if len(input_text[item]) != 7:
                print(input_text)
                # if it is greater or less than 5, then it is not something our program should recognize. we need
                # to throw a warning or something.
                print(input_text[item], " is an invalid command!16")
                self.GUI.insert_output(input_text[item] + " is an invalid command!")
                # not sure if we should exit here or continue forward. I'll ask you guys.
            elif input_text[item][0] == "-" or input_text[item][0] == "+":
                if input_text[item][0] == "-":
                    temp_bool = False
                else:
                    temp_bool = True
                try:
                    int(input_text[item][1:6])  # checks if the inside can be made ints since our words will be ints.
                    if item <= 9:
                        self.memory_dict["00" + str(item)] = [temp_bool, input_text[item][1:7]]
                        self.instruction_amount += 1
                    if item > 9 and item < 100:
                        self.memory_dict["0" + str(item)] = [temp_bool, input_text[item][1 :7]]
                        self.instruction_amount += 1
                    else:
                        self.memory_dict[str(item)] = [temp_bool, input_text[item][1:7]]
                        self.instruction_amount += 1
                except ValueError:
                    self.GUI.insert_output(input_text[str(item)] + " is an invalid command!")
                    print(input_text[str(item)], " is an invalid command! 31")
            else:
                self.GUI.insert_output(input_text[item] + " is an invalid command!")
                print(input_text[item], " is an invalid command!33")
        # begins to process each instruction

        instruction_line = 0  # index for the instruction we're on
        while instruction_line < 250:
            temp_reg = str(instruction_line)
            if instruction_line <= 9:
                temp_instruction = self.memory_dict[f"00{instruction_line}"]
                temp_reg = f"00{instruction_line}"
            elif instruction_line > 9 and instruction_line < 100:
                temp_instruction = self.memory_dict[f"0{instruction_line}"]
                temp_reg = f"0{instruction_line}"
            else:
                temp_instruction = self.memory_dict[temp_reg]
            if not temp_instruction[0]:
                instruction_line += 1
                pass
            else:
                our_instruction = temp_instruction[1][0:3]
                our_register = temp_instruction[1][3:]
                if our_instruction == "040":
                    instruction_line = int(our_register)
                elif our_instruction == "041":
                    instruction_line = self.BranchNeg(instruction_line, int(our_register))
                elif our_instruction == "042":
                    instruction_line = self.BranchZero(instruction_line, int(our_register))
                elif our_instruction == "043":
                    break  # break out of the loop if we reach a halt.
                else:
                    self.process_instructions(our_instruction, our_register)
                    instruction_line += 1  # incrament
        if self.test_bool is False:
            self.GUI.insert_output("\nFinished!")

    def process_instructions(self, our_instruction, our_register):
        if our_instruction == "010":  # call Read
            # passes in the register which needs to be assigned the input
            self.GUI.Read(our_register)
        elif our_instruction == "011":  # call Write.
            # passes in the register whose contents should be read.
            self.GUI.Write(our_register)
        elif our_instruction == "020":  # call Load
            # passes in register contents which must be loaded into the accumulator
            self.Load(self.memory_dict[our_register])
        elif our_instruction == "021":  # call Store
            # passes in register who will have the contents from the accumulator
            self.Store(our_register)
        elif our_instruction == "030":  # call ADD
            # passes in register contents that needs to be added to accumulator.
            # leave result in the accumulator
            self.Calc.Add(self.memory_dict[our_register][1])
        elif our_instruction == "031":  # call Subtract
            # passes in register contents that needs to be subtracted to accumulator.
            # leave result in the accumulator
            self.Calc.Subtract(self.memory_dict[our_register][1])
        elif our_instruction == "032":  # call Divide
            # passes in register contents that needs to be Divided to accumulator.
            # leave result in the accumulator
            self.Calc.Divide(self.memory_dict[our_register][1])
        elif our_instruction == "033":  # call Multiply
            # passes in register contents that needs to be multiplied to accumulator.
            # leave result in the accumulator
            self.Calc.Multiply(self.memory_dict[our_register][1])
        else:
            # I don't know what to do with these since they're not instructions.
            # self.memory_dict[our_register][0] = False
            pass

    def BranchNeg(self, instruction_line, our_register):
        '''Branch negative method. If accumulator is negative branch to specific
        register location otherwise, keep going throuhg the program as normal.'''
        if int(self.accumulator[1]) < 0:
            instruction_line = our_register  # branch to specific mem location
            return instruction_line

        instruction_line += 1  # incrament the instruction line to go to next instruction
        return instruction_line

    def BranchZero(self, instruction_line, our_register):
        '''Branch Zero method. If accumulator is zero branch to specific
           register location otherwise, keep going throuhg the program as normal'''
        if int(self.accumulator[1]) == 0:
            instruction_line = our_register  # branch to specific mem location
            return instruction_line

        instruction_line += 1  # incrament the instruction line to go to next instruction
        return instruction_line

    # validates input from user. if it is not a valid file path, it asks for a new file path.


    def Load(self, val):
        '''load a word from a specific location in memory(val) into the accumulator'''
        self.accumulator = val

    def Store(self, val):
        '''store a word from the accumulator into a specific location(val) in memory'''
        self.memory_dict[val] = self.accumulator


def main():
    uvs = UVSim()



if __name__ == '__main__':
    main()
