from tkinter import colorchooser
from tkinter import *


class UVSimGUIColor:
    def __init__(self, GUI):
        self.GUI = GUI

    def ChangePrimaryColor(self):
        self.GUI.primary_color = colorchooser.askcolor(title="Choose Primary Color")[1]
        self.GUI.primary_color_button.configure(background=self.GUI.primary_color)
        self.UpdateColors()

    def ChangeSecondaryColor(self):
        self.GUI.secondary_color = colorchooser.askcolor(title="Choose Secondary Color")[1]
        self.GUI.secondary_color_button.configure(background=self.GUI.secondary_color)
        self.UpdateColors()

    def ChangeTertiaryColor(self):
        self.GUI.tertiary_color = colorchooser.askcolor(title="Choose Tertiary Color")[1]
        self.GUI.tertiary_color_button.configure(background=self.GUI.tertiary_color)
        self.UpdateColors()

    def ChangeTextColor(self):
        self.GUI.text_color = colorchooser.askcolor(title="Choose Text Color")[1]
        self.GUI.text_color_button.configure(background=self.GUI.text_color)
        self.UpdateColors()

    def ChangeSecondaryTextColor(self):
        self.GUI.secondary_text_color = colorchooser.askcolor(title="Choose Secondary Text Color")[1]
        self.GUI.secondary_text_color_button.configure(background=self.GUI.secondary_text_color)
        self.UpdateColors()

    def ChangeOutputBG(self):
        self.GUI.output_bg = colorchooser.askcolor(title="Choose Secondary Text Color")[1]
        self.GUI.output_color_button.configure(background=self.GUI.output_bg)
        self.UpdateColors()

    def ChangeOutputText(self):
        self.GUI.output_text_color = colorchooser.askcolor(title="Choose Secondary Text Color")[1]
        self.GUI.secondary_text_color_button.configure(background=self.GUI.secondary_text_color)
        self.UpdateColors()

    def ResetColorsToDefault(self):
        self.GUI.primary_color = self.GUI.default_primary_color
        self.GUI.secondary_color = self.GUI.default_secondary_color
        self.GUI.tertiary_color = self.GUI.default_tertiary_color
        self.GUI.text_color = self.GUI.default_text_color
        self.GUI.secondary_text_color = self.GUI.default_secondary_text_color

    def UpdateColors(self):
        self.GUI.style_Main.configure("Main Style", foreground=self.GUI.primary_color, background=self.GUI.text_color)
        self.GUI.style_dom_button.configure("Main Style Dom Button", foreground=self.GUI.secondary_color, background=self.GUI.text_color)
        self.GUI.style_sub_button.configure("Main Style Sub Button", foreground=self.GUI.tertiary_color, background=self.GUI.secondary_text_color)

        our_guys = self.GUI.our_window.winfo_children()
        for guy in our_guys:
            if guy.cget("style") == "Main Style":
                guy.configure(style="Main Style")
            elif guy.cget("style") == "Main Style Dom Button":
                guy.configure(style="Main Style Dom Button")
            elif guy.cget("style") == "Main Style Sub Button":
                guy.configure(style="Main Style Sub Button")


