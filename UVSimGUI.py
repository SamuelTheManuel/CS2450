import os.path
from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from pathlib import Path

import PIL
import PIL.Image
from PIL import ImageTk

from UVSimGUIColor import UVSimGUIColor


class UVSimGUI:
    def __init__(self, UVSim, test_bool):
        self.line_limit = 10
        self.UVS = UVSim
        self.test_bool = test_bool
        self.style_dict = []
        self.cut_file_name = ""

        self.default_primary_color = "#78be20"
        self.default_secondary_color = "#275D38"
        self.default_tertiary_color = "#a7a8aa"
        self.default_text_color = "#FFFFFF"
        self.default_secondary_text_color = "#000000"
        self.default_output = "#ffffff"
        self.default_output_text = "#000000"
        self.Error_message = None

        if self.test_bool is False:
            self.filename = ""
            self.primary_color = "#78be20"
            self.secondary_color = "#275D38"
            self.text_color = "#FFFFFF"
            self.secondary_text_color = "#000000"
            self.tertiary_color = "#a7a8aa"
            self.output_bg = "#ffffff"
            self.output_text = "#000000"
            self.initialize_GUI()

    def initialize_GUI(self):
        mod_int = 20
        self.our_window = Tk()
        self.our_window.title("UVSim")
        self.our_window.resizable(False, False)
        self.our_window.geometry('600x300')
        self.our_window.configure(bg=self.primary_color, highlightcolor=self.tertiary_color)

        # open file button
        self.open_file_button = Button(self.our_window, text="Choose instruction file:  ", command=self.select_file)
        self.open_file_button.configure(background=self.secondary_color, font=("Constantia", "10"), foreground=self.text_color)
        self.open_file_button.bind("<Enter>", self.on_enter)
        self.open_file_button.bind("<Leave>", self.on_exit)
        self.open_file_button.place(x=75, y=60 + mod_int)
        self.style_dict.append([self.open_file_button, "Secondary", "Text"])

        # new file button
        self.new_file_button = Button(self.our_window, text="New File:", command=self.new_file)
        self.new_file_button.configure(background=self.secondary_color, font=("Constantia", "10"), foreground=self.text_color)
        self.new_file_button.bind(("<Enter>"), self.on_enter)
        self.new_file_button.bind("<Leave>", self.on_exit)
        self.new_file_button.place(x=155, y=100 + mod_int)
        self.style_dict.append([self.new_file_button, "Secondary", "Text"])

        # Edit file button
        self.edit_file_button = Button(self.our_window, text="Edit File:", command=self.edit_file_setup)
        self.edit_file_button.configure(background=self.tertiary_color, font=("Constantia", "10"), foreground=self.secondary_text_color)
        self.edit_file_button.bind(("<Enter>"), self.on_enter)
        self.edit_file_button.bind("<Leave>", self.on_exit)
        self.edit_file_button.place(x=85, y=100 + mod_int)
        self.style_dict.append([self.edit_file_button, "Tertiary", "SecondaryText"])

        #filemenu
        self.menubar = Menu(self.our_window)
        self.file_menu = Menu(self.menubar, tearoff=0, title="File")
        self.file_menu.add_command(label="Color Preferences", command=self.ChangeColors)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.our_window.config(menu=self.menubar)

        # process instructions file
        self.enter_button = Button(self.our_window, text="Run Program", command=self.process_file)
        self.enter_button.configure(bg=self.tertiary_color, font=("Constantia", "10"), foreground=self.secondary_text_color)
        self.enter_button.bind("<Enter>", self.on_enter)
        self.enter_button.bind("<Leave>", self.on_exit)
        self.enter_button.place(x=105, y=140 + mod_int)
        self.style_dict.append([self.enter_button, "Tertiary", "SecondaryText"])


        #logo
        self.uvsimLogo = PIL.Image.open("UVSim_Logo.png")
        self.uvsimLogo = self.uvsimLogo.resize(size=(100, 50))
        self.render = ImageTk.PhotoImage(self.uvsimLogo)
        self.logo = Label(image=self.render, borderwidth=0)
        self.logo.place(x=100, y=0 + mod_int)

        #Label:
        self.our_label = Label(self.our_window, text="Selected File: ", font=("Constantia", 10), background=self.primary_color, foreground=self.secondary_text_color)
        self.our_label.place(x=20, y=270)
        self.style_dict.append([self.our_label, "Primary", "SecondaryText"])


        v = Scrollbar(self.our_window, orient="vertical")
        self.our_output = Text(self.our_window, font=("Constantia", 10), yscrollcommand=v.set, background=self.output_bg, foreground=self.output_text, width=35, height=14)
        self.our_output.insert(CURRENT, "Output: ")
        self.our_output.configure(state="disabled")
        v.config(command=self.our_output.yview)
        self.our_output.place(x=300, y=50)
        self.style_dict.append([self.our_output, "OutputBg", "OutputText"])


        self.memory_button = Button(self.our_window, font=("Constantia", 10), text="Display Register Contents", command=self.display_memory, background=self.secondary_color, foreground=self.text_color)
        self.memory_button.bind("<Enter>", self.on_enter)
        self.memory_button.bind("<Leave>", self.on_exit)
        self.memory_button.place(x=300, y=20)
        self.style_dict.append([self.memory_button, "Secondary", "Text"])


        self.initialize_memory_button = Button(self.our_window, font=("Constantia", 10), text="Reset Memory", command=self.UVS.initialize_memory, background=self.tertiary_color, foreground=self.secondary_text_color)
        self.initialize_memory_button.bind("<Enter>", self.on_enter)
        self.initialize_memory_button.bind("<Leave>", self.on_exit)
        self.initialize_memory_button.place(x=460, y=20)
        self.style_dict.append([self.initialize_memory_button, "Tertiary", "SecondaryText"])

    def select_file(self):
        allowed_file_types = [('text files', "*.txt")]
        self.filename = fd.askopenfilename(title="Choose your instruction .txt file: ", initialdir='/', filetypes=allowed_file_types)
        self.our_label.configure(text="Selected File: " + self.filename)
        self.insert_output("----------------------" + "\nSelected File: " + self.filename + "\n")

    def process_file(self):
        if self.filename == "":
            self.insert_output("Please Try again! Invalid File.")
        else:
            our_string = self.input_validation(self.filename).strip().split()
        
            if len(our_string[0]) == 5:
                our_string = self.translation(our_string)
            if our_string == "Please try again!":
                pass
            else:
                self.UVS.initiate_process(our_string)

    def user_input_setup(self):
        self.input_window = Toplevel(self.our_window)
        self.input_window.title("Input: ")
        self.input_window.geometry("300x75")
        self.input_window.configure(background=self.primary_color)
        self.input_window.grab_set()
        self.style_dict.append([self.input_window, "Primary", "Text"])


        self.label = Label(self.input_window, text="Please Input a 6 character word. I.E. 012345", font=("Constantia", 10), background=self.output_bg, foreground=self.output_text)
        self.label.pack()
        self.style_dict.append([self.label, "OutputBg", "OutputText"])


        self.entry = Entry(self.input_window, width=30, background=self.output_bg, foreground=self.output_text, insertbackground=self.output_bg)
        self.style_dict.append([self.entry, "OutputBG", "OutputText"])


        #entry
        self.entry.focus_set()
        self.entry.pack()

        #button
        self.our_button = Button(self.input_window, text="Enter", command=self.enter_button_set, background=self.secondary_color, foreground=self.text_color)
        self.our_button.bind("<Enter>", self.on_enter)
        self.our_button.bind("<Leave>", self.on_exit)
        self.style_dict.append([self.open_file_button, "Secondary", "Text"])
        self.our_button.pack()

    def user_input(self):
        self.var = IntVar()
        self.our_button.wait_variable(self.var)
        self.input_enter_press = False
        return self.our_input

    def enter_button_set(self):
        self.our_input = self.entry.get()
        self.insert_output(self.our_input + "\n")
        self.var.set(1)
        self.our_button.destroy()
        self.label.destroy()
        self.entry.destroy()
        self.input_window.destroy()

    def insert_output(self, output_string):
        self.our_output.configure(state="normal")
        self.our_output.insert(END, "\n" + str(output_string))
        self.our_output.configure(state="disabled")

    def display_memory(self):
        self.insert_output("\n")
        for register in self.UVS.memory_dict:
            self.insert_output("Register: " + f"{register} - Contents: " + f"{self.UVS.memory_dict[register][1]}")
        self.insert_output("\n")

    def Read(self, register):
        # instrucion 010 Read a word from the keyboard into a specific location in memory.
        # A word is a signed four-digit decimal number, such as +1234, -5678.
        if int(register)>250:
            print("invalid register number. Resgister limit 250")
        else:
            if self.test_bool is False:
                self.user_input_setup()
                input_text = self.user_input()
            else:
                input_text = input("Please input a six-digit value: ")
            try:
                temp = int(input_text.strip())
                while (not (isinstance(temp, int) and len((input_text))) == 6):
                    if self.test_bool is False:
                        self.insert_output(input_text + " is an invalid word!")
                        input_text = self.user_input()
                    else:
                        print("Invalid input!")
                        input_text = input("Please try again. (I.e. 012345 or 024321): ")
                    temp = int(input_text)
                self.UVS.memory_dict[register] = [False, input_text]
                return self.UVS.memory_dict[register]
            except ValueError:
                if self.test_bool is False:
                    self.insert_output(input_text + " is an invalid word!")
                else:
                    print(f"{input_text} is an invalid word!")
                self.Read(register)

    def Write(self, register):
        # instruciton 011 Write a word from a specific location in memory to screen.
        # self.memory_dict[int(val)] = [True, self.accumulator]
        if register in self.UVS.memory_dict:
            if self.test_bool is False:
                self.insert_output(f'{self.UVS.memory_dict[register][1]}')
            else:
                print(f'{self.UVS.memory_dict[register][1]}')
            return {self.UVS.memory_dict[register][1]}

    def input_validation(self, our_input=None):
        """
        Validates user input. Valid input is an existing file path.
        :return: the text within that file as a string.
        """
        args = our_input
        try:
            if args is None:
                our_string = ""
                args = input("Please provide full input file path here: ")  # takes user input
            if args == "quit":  # ends program
                exit()
            with open(args, "r") as input_file:  # attempts to open the file given
                our_string = input_file.read()
            return our_string
        except FileNotFoundError:  # if the file doesn't exist, retry.
            return "Please try again!"

    def translation(self,input):
        for i in range(len(input)):
            input[i] = input[i][:3] + '0' + input[i][3:]
            input [i] =input[i][:1] +'0' + input[i][1:]
        return input

    def on_enter(self, e):
        e.widget["foreground"], e.widget["background"] = e.widget["background"], e.widget["foreground"]

    def on_exit(self, e):
        e.widget["foreground"], e.widget["background"] = e.widget["background"], e.widget["foreground"]

    def new_file(self):
        self.filename = ""
        self.cut_file_name = "Edit File: "
        self.edit_file()

    def edit_file_setup(self):
        self.select_file()
        self.cut_file_name = os.path.basename(self.filename)
        self.edit_file()

    def edit_file(self):
        self.input_widget = Toplevel(self.our_window)
        self.input_widget.title(self.cut_file_name)
        self.input_widget.geometry("400x330")
        self.input_widget.configure(background="#ffffff")
        #self.input_widget.grab_set()

        v = Scrollbar(self.input_widget, orient="vertical")
        self.file_edit = Text(self.input_widget, font=("Constantia", 10), yscrollcommand=v.set,
                               background=self.output_bg, foreground=self.output_text, width=35, height=14)
        v.config(command=self.file_edit.yview)
        self.line_num = Label(self.input_widget, text=("Line: " + str(int(self.file_edit.index(INSERT).split(".")[0]) - 1)),
                              foreground=self.primary_color, background=self.text_color)

        self.file_edit.bind('<KeyRelease>', self.LineChange)
        self.file_edit.bind('<ButtonRelease>', self.LineChange)

        self.style_dict.append([self.line_num, "Primary", "Text"])

        self.file_edit.focus()
        self.line_num.pack()

        self.file_edit.pack()
        self.style_dict.append([self.our_output, "OutputBg", "OutputText"])

        #save File Button
        self.save_file_button = Button(self.input_widget, background=self.secondary_color, foreground=self.text_color, command=self.SaveFile, text="Save File")
        self.save_file_button.bind("<Enter>", self.on_enter)
        self.save_file_button.bind("<Leave>", self.on_exit)
        self.save_file_button.pack()
        self.style_dict.append([self.save_file_button, "Secondary", "Text"])

        #cancel Button
        self.cancel_button = Button(self.input_widget, background=self.secondary_color, foreground=self.text_color, text="Cancel",
                                       command=self.input_widget.destroy)
        self.cancel_button.bind("<Enter>", self.on_enter)
        self.cancel_button.bind("<Leave>", self.on_exit)
        self.cancel_button.pack()
        self.style_dict.append([self.cancel_button, "Secondary", "Text"])

        #save and run button
        self.cancel_button = Button(self.input_widget, background=self.secondary_color, foreground=self.text_color, text="Save and Run",
                                       command=self.save_and_run)
        self.cancel_button.bind("<Enter>", self.on_enter)
        self.cancel_button.bind("<Leave>", self.on_exit)
        self.cancel_button.pack()
        self.style_dict.append([self.cancel_button, "Secondary", "Text"])

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    self.file_edit.insert(END, line)
        except FileNotFoundError or Exception:
            pass

    def SaveFile(self):
        nlCount = 0
        lyst = self.file_edit.get(1.0, END)
        for line in lyst:
            if line == "\n":
                nlCount += 1
        if nlCount > self.line_limit:
           self.ErrorMessageSave("Too many lines- won't fit in register! Will result in Error!")

        f = asksaveasfile(initialfile='Untitled.txt',
                          defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        try:
            f.write(self.file_edit.get(1.0, END))
            self.filename = f.name
            self.our_label.configure(text="Selected File: " + self.filename)
            self.insert_output("----------------------" + "\nSelected File: " + self.filename + "\n")
            f.close()
            return True
        except AttributeError:
            self.ErrorMessageSave("Save Failed!")
            return False

    def LineChange(self, idk):
        self.line_num.config(text=("Line: " + str(int(self.file_edit.index(INSERT).split(".")[0]) - 1)))
        if int(float(self.file_edit.index(INSERT.split(".")[0]))) > self.line_limit:
            self.ErrorMessageSave("Too many lines!")
            self.file_edit.mark_set("insert", "%d.%d" % (0, 0))

    def ErrorMessageSave(self, ourText):
        self.Error_message = Toplevel(self.input_widget)

        self.Error_message.configure(background="#ffffff")
        self.Error_message.title("Warning!")
        self.Error_message.geometry("200x30")

        self.Error_Text = Label(self.Error_message, text=ourText,
                           foreground="black")
        self.Error_Text.pack()

    def ChangeColors(self):
        self.color_select = Toplevel(self.our_window)
        self.color_select.title("Colors: ")
        self.color_select.geometry("300x400")
        self.color_select.configure(background="#ffffff")
        self.color_select.grab_set()

        self.GUIColor = UVSimGUIColor(self)
        self.reset_all_color_button = Button(self.color_select,font=("Constantia", 15), background=self.default_primary_color, foreground="white", text="Reset to Default", command=self.GUIColor.ResetColorsToDefault)
        self.primary_color_button = Button(self.color_select,font=("Constantia", 15), background=self.primary_color, foreground=self.text_color, text="Primary Color: ", command=self.GUIColor.ChangePrimaryColor)
        self.secondary_color_button = Button(self.color_select,font=("Constantia", 15), background=self.secondary_color, foreground=self.text_color, text="Secondary Color: ", command=self.GUIColor.ChangeSecondaryColor)
        self.tertiary_color_button = Button(self.color_select,font=("Constantia", 15), background=self.tertiary_color, foreground=self.secondary_text_color, text="Tertiary Color: ", command=self.GUIColor.ChangeTertiaryColor)
        self.text_color_button = Button(self.color_select,font=("Constantia", 15), background=self.text_color, foreground=self.primary_color, text="Text Color: ", command=self.GUIColor.ChangeTextColor)
        self.secondary_text_button = Button(self.color_select,font=("Constantia", 15), background=self.secondary_text_color, foreground=self.tertiary_color, text="Secondary Text Color: ", command=self.GUIColor.ChangeSecondaryTextColor)
        self.output_color_button = Button(self.color_select, text= "Output Box", font=("Constantia", 15), background=self.output_bg, foreground=self.primary_color, command=self.GUIColor.ChangeOutputBG)
        self.output_text_button = Button(self.color_select, text="Output Text", font=("Constantia", 15), background=self.output_text, foreground= self.secondary_color, command=self.GUIColor.ChangeOutputText)

        self.style_dict.append([self.primary_color_button, "Primary", "Text"])
        self.style_dict.append([self.secondary_color_button, "Secondary", "Text"])
        self.style_dict.append([self.tertiary_color_button, "Tertiary", "SecondaryText"])
        self.style_dict.append([self.text_color_button, "Text", "Primary"])
        self.style_dict.append([self.secondary_text_button, "SecondaryText", "Tertiary"])
        self.style_dict.append([self.output_color_button, "OutputBg", "Primary"])
        self.style_dict.append([self.output_text_button, "OutputText", "Secondary"])



        self.reset_all_color_button.bind("<Enter>", self.on_enter)
        self.reset_all_color_button.bind("<Leave>", self.on_exit)
        self.primary_color_button.bind("<Enter>", self.on_enter)
        self.primary_color_button.bind("<Leave>", self.on_exit)
        self.secondary_color_button.bind("<Enter>", self.on_enter)
        self.secondary_color_button.bind("<Leave>", self.on_exit)
        self.secondary_text_button.bind("<Enter>", self.on_enter)
        self.secondary_text_button.bind("<Leave>", self.on_exit)
        self.tertiary_color_button.bind("<Enter>", self.on_enter)
        self.tertiary_color_button.bind("<Leave>", self.on_exit)
        self.text_color_button.bind("<Enter>", self.on_enter)
        self.text_color_button.bind("<Leave>", self.on_exit)
        self.output_color_button.bind("<Enter>", self.on_enter)
        self.output_color_button.bind("<Leave>", self.on_exit)
        self.output_text_button.bind("<Enter>", self.on_enter)
        self.output_text_button.bind("<Leave>", self.on_exit)

        self.reset_all_color_button.pack()
        self.primary_color_button.pack()
        self.secondary_color_button.pack()
        self.tertiary_color_button.pack()
        self.text_color_button.pack()
        self.secondary_text_button.pack()
        self.output_color_button.pack()
        self.output_text_button.pack()

    def save_and_run(self):
        if(self.SaveFile()):
            self.process_file()
        else:
            self.ErrorMessageSave("Error with save!")
