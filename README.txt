-------------------------------------------------------------
UVSIM:

Requirements:
Install Python
Install pytest for unit tests
Install mock for unit tests
Install PIL

How to use: 
Run the UVSimBaseCode.py file with all other files in same directory. The GUI will then launch showing you the program and its different functions. At any time, clicking the "display register contents" button will print out each register and its contents in the output box. Clicking the "Reset Memory" button will clear the memory, initializing each register to 0000.

To run an instruction file through the UVSim, click the "Choose your instruction .txt file:" button, find and open the .txt file to be processed through the pop-up files menu, then click the "Enter" button.

The program will run your instructions given by the chosen .txt file and prompt you to enter any needed inputs after a read instruction is processed.

To change the colors of the GUI, click File > Color Preferences. This will open up a menu showing the current colors and the options available. Simply select the one you'd like to change and pick a color from the menu. Click "Reset to Default" to change the colors back to the default UVU colors.

To edit the current instruction file, click "Edit File:". This will open up a menu with a text box for you to add up to 100 instructions for the UV Sim. You will then save the file and the UVSim will have the file to run when prompted through "Run Program". To create a new instruction file, click the "New File:" button and enter in your instructions and save it.

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

Arithmetic operations:
ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operations:
BRANCH = 40 Branch to a specific location in memory
BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.
HALT = 43 Pause the program

