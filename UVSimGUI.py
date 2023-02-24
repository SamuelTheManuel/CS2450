import tkinter.font
from tkinter import *
from tkinter import filedialog as fd
import PIL
import PIL.Image
from PIL import ImageTk


class UVSimGUI:
    def __init__(self, UVSim):
        self.UVS = UVSim
        self.initialize_GUI()
        self.button = Button(text="Enter", command=self.process_file)
        self.filename = ""

    def initialize_GUI(self):
        mod_int = 20
        self.our_window = Tk()
        self.our_window.title("UVSim")
        self.our_window.resizable(False, False)
        self.our_window.geometry('600x300')
        self.our_window.configure(bg="#9EE493", highlightcolor="#503D3F")

        # open file button
        self.open_file_button = Button(self.our_window, text="Choose your instruction .txt file:  ", command=self.select_file)
        self.open_file_button.configure(bg="#065143", font=("Constantia", "10"), foreground="#FFFFFF", relief="flat")
        self.open_file_button.place(x=20, y=140 + mod_int)

        # process instructions file
        self.enter_button = Button(self.our_window, text="Enter", command=self.process_file)
        self.enter_button.configure(bg="#503D3F", font=("Constantia", "10"), foreground="#FFFFFF", relief="flat")
        self.enter_button.place(x=100, y=180 + mod_int)

        #logo
        self.uvsimLogo = PIL.Image.open("UVSim_Logo.png")  
        self.uvsimLogo = self.uvsimLogo.resize(size=(202, 101))
        self.render = ImageTk.PhotoImage(self.uvsimLogo)
        self.logo = Label(image=self.render, borderwidth=0)
        self.logo.place(x=20, y=20 + mod_int)

        #Label:
        self.our_label = Label(text="Selected File: ", font=("Constantia", 10), background="#128490", foreground="#FFFFFF")
        self.our_label.place(x=20, y=260)

        v = Scrollbar(self.our_window, orient="vertical")
        self.our_output = Text(self.our_window, font=("Constantia", 10), yscrollcommand=v.set, background="#FFFFFF", foreground="#129490", width=35, height=14)
        self.our_output.insert(CURRENT, "Output: ")
        self.our_output.configure(state="disabled")
        v.config(command=self.our_output.yview)
        self.our_output.place(x=300, y=20 + mod_int)

        self.memory_button = Button(self.our_window, font=("Constantia", 10), text="Display Register Contents", command=self.display_memory, background="#065143", foreground="#9EE493", relief="flat")
        self.memory_button.place(x=300, y=5)

        self.initialize_memory_button = Button(self.our_window, font=("Constantia", 10), text="Reset Memory", command=self.UVS.initialize_memory, background="#128490", foreground="#FFFFFF", relief="flat")
        self.initialize_memory_button.place(x=460, y=5)

    def select_file(self):
        allowed_file_types = [('text files', "*.txt")]
        self.filename = fd.askopenfilename(title="Choose your instruction .txt file: ", initialdir='/', filetypes=allowed_file_types)
        self.our_label.configure(text="Selected File: " + self.filename)
        self.insert_output("----------------------" + "\nSelected File: " + self.filename + "\n")

    def process_file(self):
        if self.filename == "":
            self.insert_output("Please Try again! Invalid File.")
        else:
            our_string = self.UVS.input_validation(self.filename).strip().split()
            if our_string == "Please try again!":
                pass
            else:
                self.UVS.initiate_process(our_string)

    def user_input_setup(self):
        self.input_window = Toplevel(self.our_window)
        self.input_window.title("Input: ")
        self.input_window.geometry("300x75")
        self.input_window.configure(background="#50343F")
        self.input_window.grab_set()

        self.label = Label(self.input_window, text="Please Input a 4 character word. I.E. 0234", font=("Constantia", 10), background="#50343F", foreground="#9EE493")
        self.label.pack()

        self.entry = Entry(self.input_window, width=30, background="#FFFFFF", foreground="#50343F", insertbackground="#FFFFFF")

        #entry
        self.entry.focus_set()
        self.entry.pack()

        #button
        self.our_button = Button(self.input_window, text="Enter", command=self.enter_button_set, background= "#9EE493", foreground="#50343F", relief="flat")
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



