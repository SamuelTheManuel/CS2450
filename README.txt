-------------------------------------------------------------
UVSIM:

Requirements:
Install Python
Install pytest for unit tests
Install mock for unit tests

How to use: 
Put any .txt file(s) with instructions in same directory as UVSimBaseCode.py. From the command line, navigate to this parent directory. Once there, type: python UVSimBaseCode.py. This will run the program.

When prompted, enter file path (relative or absolute) of the .txt file to be processed. 

example: 
Please provide full input file path here: ./Test1.txt

The program will run your instructions given by the .txt file and prompt you to enter any needed inputs.

If a read instruction is submitted, input a 4 digit integer (word). 
C:\Users\Sarah Keeley\Desktop\Sarah\school\Coding\ExampleInstructions.txt 


example.txt :
-------------------------------------------------------------
+1009
+1010
+2009
+3110
+4107
+1109
+4300
+1110
+4300
+0000
+0000
-99999
-------------------------------------------------------------
In the above example, the -99999 would be an invalid input and skipped over. 

Instructions:
Instructions must be preceded by a +. The first two digits specify the operation to be performed. The last two digits specify the memory location on which the operation is performed. Ex. +1030 will read a word from the keyboard into memory location 30.

READ = 10 Read a word from the keyboard into a specific location in memory.
WRITE = 11 Write a word from a specific location in memory to screen.

Load/store operations:
LOAD = 20 Load a word from a specific location in memory into the accumulator.
STORE = 21 Store a word from the accumulator into a specific location in memory.

Arithmetic operation:
ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operation:
BRANCH = 40 Branch to a specific location in memory
BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.
HALT = 43 Pause the program

