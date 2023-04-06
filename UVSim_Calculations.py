class UVSim_Calculations:
    def __init__(self, UVSimBaseCode):
        self.UVS = UVSimBaseCode

    def Add(self, register_word):
        '''Add a word from a given register in memory to the word in the accumulator.
        Result is stored in the accumulator'''
        accumulator = self.UVS.accumulator[1]
        new_accumulator = str(int(accumulator) + int(register_word))
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 7:
            if new_accumulator[1][0] == '-':
                new_accumulator[1] = '-0' + new_accumulator[1][1:]
            else:
                new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0 and new_accumulator[1][0] == '0':
            new_accumulator[1] = new_accumulator[1][1:]
        self.UVS.accumulator = new_accumulator  # store result in accumulator

    def Subtract(self, register_word):
        '''Subtract a word from a given register in memory from the word in the accumulator.
        Result is stored in the accumulator'''
        accumulator = self.UVS.accumulator[1]
        new_accumulator = str(int(accumulator) - int(register_word))
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 7:
            if new_accumulator[1][0] == '-':
                new_accumulator[1] = '-0' + new_accumulator[1][1:]
            else:
                new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0 and new_accumulator[1][0] == '0':
            new_accumulator[1] = new_accumulator[1][1:]
        self.UVS.accumulator = new_accumulator  # store result in accumulator

    def Multiply(self, register_word):
        '''Multiply a word from a given register in memory by the word in the accumulator.
        Result is stored in the accumulator'''
        accumulator = self.UVS.accumulator[1]
        new_accumulator = str(int(accumulator) * int(register_word))
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 7:
            if new_accumulator[1][0] == '-':
                new_accumulator[1] = '-0' + new_accumulator[1][1:]
            else:
                new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0 and new_accumulator[1][0] == '0':
            new_accumulator[1] = new_accumulator[1][1:]
        self.UVS.accumulator = new_accumulator  # store result in accumulator

    def Divide(self, register_word):
        '''Divide the word in the accumulator by the word in a given register in memory.
        Result is stored in the accumulator'''
        accumulator = self.UVS.accumulator[1]
        try:
            new_accumulator = str(int(accumulator) // int(register_word))
        except ZeroDivisionError:
            print("Unable to divide by zero.")
            return "Divide by zero error"
        new_accumulator = [False, new_accumulator]
        while len(new_accumulator[1]) < 7:
            if new_accumulator[1][0] == '-':
                new_accumulator[1] = '-0' + new_accumulator[1][1:]
            else:
                new_accumulator[1] = "0" + new_accumulator[1]
        if int(new_accumulator[1]) >= 0 and new_accumulator[1][0] == '0':
            new_accumulator[1] = new_accumulator[1][1:]
        self.UVS.accumulator = new_accumulator  # store result in accumulator
