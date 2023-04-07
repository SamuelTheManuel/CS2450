-------------------------------------------------------------
UVSIM:

Requirements:
Install Python
Install pytest for unit tests
Install mock for unit tests
Install PIL

How to use: 
Run the UVSimBaseCode.py file with all other files in same directory. The GUI will then launch showing you the program and its different functions. At any time, clicking the "Display Register Contents" button will print out each register and its contents in the output box. Clicking the "Reset Memory" button will clear the memory, initializing each register to 000000.

To run an instruction file through the UVSim, click the "Choose instruction file:" button, find and open the .txt file to be processed through the pop-up files menu, then click the "Run Program" button.

The program will run your instructions given by the chosen .txt file and prompt you to enter any needed inputs after a read instruction is processed. Write instructions will output the value in the white output box.

To change the colors of the GUI, click File > Color Preferences. This will open up a menu showing the current colors and the options available. Simply select the one you'd like to change and pick a color from the menu. Click "Reset to Default" to change the colors back to the default UVU colors.

To edit an instruction file, click "Edit File:". This will allow you to choose a file to edit and open up a menu with a text box for you to modify up to 250 lines of instructions for the UVSim. You will then save the file and it will be available to choose for processing. You can also run it immediately by clicking "Save and Run". 

To create a new instruction file, click the "New File:" button, enter in your instructions, and click "Save File". You may have multiple files open at the same time to modify.

example.txt :
-------------------------------------------------------------
+010009
+010010
+020009
+031010
+041007
+011009
+043000
+011010
+043000
+000000
+000000
-0099999
-------------------------------------------------------------
In the above example, the -0099999 would be an invalid input and skipped over. 

Instructions:
Instructions must be preceded by a +. The first three digits specify the operation to be performed. The last three digits specify the memory location on which the operation is performed. Ex. +010030 will read a word from the keyboard into memory location 030.

READ = 010 Read a word from the keyboard into a specific location in memory.
WRITE = 011 Write a word from a specific location in memory to screen.

Load/store operations:
LOAD = 020 Load a word from a specific location in memory into the accumulator.
STORE = 021 Store a word from the accumulator into a specific location in memory.

Arithmetic operations:
ADD = 030 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
SUBTRACT = 031 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
DIVIDE = 032 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
MULTIPLY = 033 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operations:
BRANCH = 040 Branch to a specific location in memory
BRANCHNEG = 041 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 042 Branch to a specific location in memory if the accumulator is zero.
HALT = 043 Pause the program

