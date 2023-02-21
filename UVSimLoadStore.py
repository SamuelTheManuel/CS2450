class UVSimLoadStore():
    def __init__(self, UVSim):
        self.UVS = UVSim
    def Load(self, val):
        '''load a word from a specific location in memory(val) into the accumulator'''
        self.UVS.accumulator = val


    def Store(self, val):
        '''store a word from the accumulator into a specific location(val) in memory'''
        self.UVS.memory_dict[val] = self.UVS.accumulator