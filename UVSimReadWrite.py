class UVSimReadWrite:
    def __init__(self, UVSimBaseCodeTest):
        self.UVS = UVSimBaseCodeTest

    def Read(self, register):
        # instrucion 10 Read a word from the keyboard into a specific location in memory.
        # A word is a signed four-digit decimal number, such as +1234, -5678.
        self.UVS.GUI.user_input_setup()
        input_text = self.UVS.GUI.user_input()
        try:
            temp = int(input_text.strip())
            while (not (isinstance(temp, int) and len((input_text))) == 4):
                self.UVS.GUI.insert_output(input_text + " is an invalid word!")
                input_text = self.UVS.GUI.user_input()
                temp = int(input_text)
            self.UVS.memory_dict[register] = [False, input_text]
            return self.UVS.memory_dict[register]

        except ValueError:
            self.UVS.GUI.insert_output(input_text + " is an invalid word!")
            self.Read(register)

    def Write(self, register):
        # instruciton 11 Write a word from a specific location in memory to screen.
        # self.memory_dict[int(val)] = [True, self.accumulator]
        if register in self.UVS.memory_dict:
            self.UVS.GUI.insert_output(f'{self.UVS.memory_dict[register][1]}')
            return ({self.UVS.memory_dict[register][1]})