import tkinter.font
from tkinter import *
from tkinter import filedialog as fd
from tkinter import colorchooser as cc
import PIL
import PIL.Image
from PIL import ImageTk

from UVSimGUIColor import UVSimGUIColor


class UVSimGUI:
    def __init__(self, UVSim, test_bool):
        self.UVS = UVSim
        self.test_bool = test_bool
        self.style_dict = []

        self.default_primary_color = "#78be20"
        self.default_secondary_color = "#275D38"
        self.default_tertiary_color = "#a7a8aa"
        self.default_text_color = "#FFFFFF"
        self.default_secondary_text_color = "#000000"
        self.default_output = "#ffffff"
        self.default_output_text = "#000000"

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


        #filemenu
        self.menubar = Menu(self.our_window)
        self.file_menu = Menu(self.menubar, tearoff=0, title="File")
        # self.file_menu.add_command(label="Save", command= EDIT this is where you can save your file? or maybe we change to new file and it opens a new dialogue to make a text document.)
        #if we do a new file option let's have it open like the text editing app on their thing maybe? probs not
        self.file_menu.add_command(label="Color Preferences", command=self.ChangeColors)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.our_window.config(menu=self.menubar)

        # process instructions file
        self.enter_button = Button(self.our_window, text="Run Program", command=self.process_file)
        self.enter_button.configure(bg=self.tertiary_color, font=("Constantia", "10"), foreground=self.secondary_text_color)
        self.enter_button.bind("<Enter>", self.on_enter)
        self.enter_button.bind("<Leave>", self.on_exit)
        self.enter_button.place(x=105, y=95 + mod_int)
        self.style_dict.append([self.enter_button, "Tertiary", "SecondaryText"])


        #logo
        self.uvsimLogo = PIL.Image.open("UVSim_Logo.png")
        self.uvsimLogo = self.uvsimLogo.resize(size=(100, 50))
        self.render = ImageTk.PhotoImage(self.uvsimLogo)
        self.logo = Label(image=self.render, borderwidth=0)
        self.logo.place(x=100, y=0 + mod_int)

        #Label:
        self.our_label = Label(self.our_window, text="Selected File: ", font=("Constantia", 10), background=self.primary_color, foreground=self.secondary_text_color)
        self.our_label.place(x=20, y=260)
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


        self.label = Label(self.input_window, text="Please Input a 4 character word. I.E. 0234", font=("Constantia", 10), background=self.output_bg, foreground=self.output_text)
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
        # instrucion 10 Read a word from the keyboard into a specific location in memory.
        # A word is a signed four-digit decimal number, such as +1234, -5678.
        if self.test_bool is False:
            self.user_input_setup()
            input_text = self.user_input()
        else:
            input_text = input("Please input a four-digit value: ")
        try:
            temp = int(input_text.strip())
            while (not (isinstance(temp, int) and len((input_text))) == 4):
                if self.test_bool is False:
                    self.insert_output(input_text + " is an invalid word!")
                    input_text = self.user_input()
                else:
                    print("Invalid input!")
                    input_text = input("Please try again. (I.e. 1234 or 0243): ")
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
        # instruciton 11 Write a word from a specific location in memory to screen.
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

    def on_enter(self, e):
        e.widget["foreground"], e.widget["background"] = e.widget["background"], e.widget["foreground"]

    def on_exit(self, e):
        e.widget["foreground"], e.widget["background"] = e.widget["background"], e.widget["foreground"]

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

