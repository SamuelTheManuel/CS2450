
class UVSim:
    def __init__(self, ):
        # dict entries are like: register_number(string): [DataBool(bool), contents(string)]. DataBool indicates whether
        # the contents are a value or not. if it is false, the contents are an instruction. if it is true, the contents
        # should be ignored.
        self.memory_dict = {}
        self.instruction_amount = 0
        self.accumulator = [False, "0000"] # this is our accumulator. We want to use this.w
        for i in range(99): #initiallizes our co
            our_key = i
            if i <= 9:
                our_key = "0" + str(our_key)
            else:
                our_key = str(our_key)
            self.memory_dict[our_key] = [True, "0000"]


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
        
        instruction_line = 0 #index for the instruction we're on
        while instruction_line < len(self.memory_dict):
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
                    instruction_line += 1 #incrament 
                
    def process_instructions(self, our_instruction, our_register):
        if our_instruction == "10":  # call Read
            # passes in the register which needs to be assigned the input
            self.Read(our_register)
        elif our_instruction == "11":  # call Write.
            # passes in the register whose contents should be read.
            self.Write(our_register)
        elif our_instruction == "20":  # call Load
            # passes in register contents which must be loaded into the accumulator
            self.Load(self.memory_dict[our_register])
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
        else:
            # I don't know what to do with these since they're not instructions.
            self.memory_dict[our_register][0] = False
        

    def Add(self, register_word):
        '''Add a word from a given register in memory to the word in the accumulator.
        Result is stored in the accumulator'''
        accumulator = self.accumulator[1]
        new_accumulator = str(int(accumulator) + int(register_word))
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 5:
            new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0:
            new_accumulator[1] = new_accumulator[1][1:]
        self.accumulator = new_accumulator # store result in accumulator

    def Subtract(self, register_word):
        '''Subtract a word from a given register in memory from the word in the accumulator.
        Result is stored in the accumulator'''
        accumulator = self.accumulator[1]
        new_accumulator = str(int(accumulator) - int(register_word))
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 5:
            new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0:
            new_accumulator[1] = new_accumulator[1][1:]
        self.accumulator = new_accumulator # store result in accumulator

    def Multiply(self, register_word):
        '''Multiply a word from a given register in memory by the word in the accumulator.
        Result is stored in the accumulator'''
        accumulator = self.accumulator[1]
        new_accumulator = str(int(accumulator) * int(register_word))
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 5:
            new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0 and int(new_accumulator[1][0] == '0'):
            new_accumulator[1] = new_accumulator[1][1:]
        self.accumulator = new_accumulator # store result in accumulator

    def Divide(self, register_word):
        '''Divide the word in the accumulator by the word in a given register in memory.
        Result is stored in the accumulator'''
        accumulator = self.accumulator[1]
        try:
            new_accumulator = str(int(accumulator) // int(register_word))
        except ZeroDivisionError:
            print("Unable to divide by zero.")
            return "Divide by zero error"
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 5:
            new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0:
            new_accumulator[1] = new_accumulator[1][1:]
        self.accumulator = new_accumulator # store result in accumulator

     def Load(self, val):
        '''load a word from a specific location in memory(val) into the accumulator'''    
        if val[1].isdigit():
            #load a word from a specific location in memory(val) into the accumulator
            self.accumulator = val
        else:
            print("The value you are trying to load is not a number")
    
    def Store(self, val):
        '''store a word from the accumulator into a specific location(val) in memory'''
        #test if the val is a string of numbers
        if self.memory_dict[val][0] == True:
            
            self.memory_dict[val] = self.accumulator#val is a string, not an int
        else:
            print("The value you are trying to store is not designated as a value")
            
    def Read(self, register):
        #instrucion 10 Read a word from the keyboard into a specific location in memory.
        #A word is a signed four-digit decimal number, such as +1234, -5678. 
        try:
            input_text = input("Enter vaild word: ")
            temp = int(input_text)
            while (not(isinstance(temp, int) and len((input_text))) == 4):
                input_text = input("please add a 4-digit number: ")
                temp= int(input_text)
                
            self.memory_dict[register] = [False, input_text]
    
        except ValueError:
            print(input_text, " is an invalid word!")
            self.Read(register)
        return self.memory_dict[register]


    def Write(self, register):
        #instruciton 11 Write a word from a specific location in memory to screen.
        # self.memory_dict[int(val)] = [True, self.accumulator]
        if register in self.memory_dict:   
            print(f'{self.memory_dict[register][1]}')
            return ({self.memory_dict[register][1]})


    def BranchNeg(self, instruction_line, our_register):
        '''Branch negative method. If accumulator is negative branch to specific 
        register location otherwise, keep going throuhg the program as normal.'''
        if int(self.accumulator[1]) < 0:
            instruction_line = our_register  #branch to specific mem location
            return instruction_line

        instruction_line += 1 #incrament the instruction line to go to next instruction
        return instruction_line

    def BranchZero(self, instruction_line, our_register):
        '''Branch Zero method. If accumulator is zero branch to specific
           register location otherwise, keep going throuhg the program as normal'''
        if int(self.accumulator[1]) == 0:
            instruction_line = our_register #branch to specific mem location
            return instruction_line
        
        instruction_line += 1 #incrament the instruction line to go to next instruction
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

