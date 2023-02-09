
class UVSim:
    def __init__(self, ):
        # dict entries are like: register_number(string): [DataBool(bool), contents(string)]. DataBool indicates whether
        # the contents are a value or not. if it is false, the contents are an instruction. if it is true, the contents
        # should be ignored.
        self.memory_dict = {}
        self.instruction_amount = 0
        self.accumulator = 0  # this is our accumulator. We want to use this.w


    def initiate_process(self, input_text):
        # loads each instruction into the corresponding register
        for item in range(len(input_text)):
            if len(input_text[item]) != 5:
                # if it is greater or less than 5, then it is not something our program should recognize. we need
                # to throw a warning or something.
                print(input_text[item], " is an invalid command!16")
                # not sure if we should exit here or continue forward. I'll ask you guys.
            elif input_text[item][0] == "-" or input_text[item][0] == "+":
                if input_text[item][0] == "-":
                    temp_bool = False
                else:
                    temp_bool = True
                try:
                    int(input_text[item][1:4])  # checks if the inside can be made ints since our words will be ints.
                    if item <= 9:
                        self.memory_dict["0" + str(item)] = [temp_bool, input_text[item][1:5]]
                        self.instruction_amount += 1
                    else:
                        self.memory_dict[str(item)] = [temp_bool, input_text[item][1:5]]
                        self.instruction_amount += 1
                except ValueError:
                    print(input_text[str(item)], " is an invalid command! 31")
            else:
                print(input_text[item], " is an invalid command!33")
        # begins to process each instruction
        
        instruction_line = 0
        while instruction_line < self.instruction_amount:
            temp_reg = str(instruction_line)
            if instruction_line <= 9:
                temp_instruction = self.memory_dict[f"0{instruction_line}"]
                temp_reg = f"0{instruction_line}"
            else:
                temp_instruction = self.memory_dict[temp_reg]
            if not temp_instruction[0]:
                pass
            else:
                our_instruction = temp_instruction[1][0:2]
                our_register = temp_instruction[1][2:4]
                if our_instruction == "40":
                    instruction_line = int(our_register)
                elif our_instruction == "41":
                    instruction_line = self.BranchNeg(instruction_line, int(our_register))
                elif our_instruction == "42":
                    instruction_line = self.BranchZero(instruction_line, int(our_register))
                elif our_instruction == "43":
                    break #break out of the loop if we reach a halt.
                else:
                    self.process_instructions(our_instruction, our_register)

    def process_instructions(self, our_instruction, our_register):
        if our_instruction == "10":  # call Read
            # passes in the register which needs to be assigned the input
            self.Read(our_register)
        elif our_instruction == "11":  # call Write.
            # passes in the register whose contents should be read.
            self.Write(our_register)
        elif our_instruction == "20":  # call Load
            # passes in register contents which must be loaded into the accumulator
            self.Load(self.memory_dict[our_register][1])
        elif our_instruction == "21":  # call Store
            # passes in register who will have the contents from the accumulator
            self.Store(our_register)
        elif our_instruction == "30":  # call ADD
            # passes in register contents that needs to be added to accumulator.
            # leave result in the accumulator
            self.Add(self.memory_dict[our_register][1])
        elif our_instruction == "31":  # call Subtract
            # passes in register contents that needs to be subtracted to accumulator.
            # leave result in the accumulator
            self.Subtract(self.memory_dict[our_register][1])
        elif our_instruction == "32":  # call Divide
            # passes in register contents that needs to be Divided to accumulator.
            # leave result in the accumulator
            self.Divide(self.memory_dict[our_register][1])
        elif our_instruction == "33":  # call Multiply
            # passes in register contents that needs to be multiplied to accumulator.
            # leave result in the accumulator
            self.Multiply(self.memory_dict[our_register][1])
            '''
        elif our_instruction == "40":  # calls Branch
            # I'm passing in the register that it wants to branch to, but I'm not sure what you'll need
            self.Branch(our_register)
        elif our_instruction == "41":  # calls BranchNeg
            # if accumulator is negative, branch. passes in the memory register.
            self.BranchNeg(our_register)
        elif our_instruction == "42":  # calls BranchZero
            # if accumulator is zero, branch. passes in the memory register.
            self.BranchZero(our_register)
            '''
        else:
            # I don't know what to do with these since they're not instructions.
            self.memory_dict[our_register][0] = False
        
    def Read(self, register):
        #instrucion 10 Read a word from the keyboard into a specific location in memory.
        #A word is a signed four-digit decimal number, such as +1234, -5678. 
        try:
            input_text = input("Enter vaild word: ")
            input_text = int(input_text)
            if isinstance(input_text, int) and len(str(abs(input_text))) == 4:
                self.memory_dict[register] = input_text
            else:
                print("please add a 4-digit number")
        except ValueError:
            print(input_text, " is an invalid word!")
        return

    def Write(self, register):
        #instruciton 11 Write a word from a specific location in memory to screen.
        # self.memory_dict[int(val)] = [True, self.accumulator]
        if register in self.memory_dict:
            print(self.memory_dict[register])
        else:
            print("Empty Memory Location")
        return

    def BranchNeg(self, instruction_line, our_register):
        '''Branch negative method. If accumulator is negative branch to specific 
        register location otherwise, keep going throuhg the program as normal.'''
        if self.accumulator < 0:
            instruction_line = our_register  #branch to specific mem location
            return branch_to

        return instruction_line

    def BranchZero(self, instruction_line, our_register):
        '''Branch Zero method. If accumulator is zero branch to specific
           register location otherwise, keep going throuhg the program as normal'''
        if self.accumulator == 0:
            instruction_line = our_register #branch to specific mem location
            return branch_to
        
        return instruction_line
        


def main():
    uvs = UVSim()
    our_string = input_validation().strip().split()
    uvs.initiate_process(our_string)


# validates input from user. if it is not a valid file path, it asks for a new file path.
def input_validation():
    """
    Validates user input. Valid input is an existing file path.
    :return: the text within that file as a string.
    """
    try:
        our_string = ""
        args = input("Please provide full input file path here: ")  # takes user input
        if args == "quit":  # ends program
            exit()
        with open(args, "r") as input_file:  # attempts to open the file given
            our_string = input_file.read()
        print(our_string)
        return our_string
    except FileNotFoundError:  # if the file doesn't exist, retry.
        print("Please try again! ")
        return input_validation()


if __name__ == '__main__':
    main()

