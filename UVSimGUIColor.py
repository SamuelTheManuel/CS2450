from tkinter import colorchooser
from tkinter import *


class UVSimGUIColor:
    def __init__(self, GUI):
        self.GUI = GUI

    def ChangePrimaryColor(self):
        primary_color = colorchooser.askcolor(title="Choose Primary Color")[1]
        self.UpdateColors(primary=primary_color)

    def ChangeSecondaryColor(self):
        secondary_color = colorchooser.askcolor(title="Choose Secondary Color")[1]
        self.UpdateColors(secondary=secondary_color)

    def ChangeTertiaryColor(self):
        tertiary_color = colorchooser.askcolor(title="Choose Tertiary Color")[1]
        self.UpdateColors(tertiary=tertiary_color)

    def ChangeTextColor(self):
        text_color = colorchooser.askcolor(title="Choose Text Color")[1]
        self.UpdateColors(textC=text_color)

    def ChangeSecondaryTextColor(self):
        secondary_text = colorchooser.askcolor(title="Choose Secondary Text Color")[1]
        self.UpdateColors(secondaryText=secondary_text)

    def ChangeOutputBG(self):
        output_BG = colorchooser.askcolor(title="Choose Secondary Text Color")[1]
        self.UpdateColors(outputBg=output_BG)

    def ChangeOutputText(self):
        output_text = colorchooser.askcolor(title="Choose Secondary Text Color")[1]
        self.UpdateColors(outputText=output_text)

    def ResetColorsToDefault(self):
        self.UpdateColors(primary=self.GUI.default_primary_color, secondary=self.GUI.default_secondary_color,
                          tertiary=self.GUI.default_tertiary_color, textC=self.GUI.default_text_color,
                          secondaryText=self.GUI.default_secondary_text_color,outputBg=self.GUI.default_output, outputText=self.GUI.default_output_text)

    def UpdateColors(self, primary=None, secondary=None, tertiary=None, textC=None, secondaryText=None, outputBg=None, outputText=None):
        our_guys = self.GUI.style_dict
        for guy in our_guys:
            if self.CheckIfColor(primary):
                self.SimplifySetColor(guy, primary, "Primary")
            if self.CheckIfColor(secondary):
                self.SimplifySetColor(guy, secondary, "Secondary")
            if self.CheckIfColor(tertiary):
                self.SimplifySetColor(guy, tertiary, "Tertiary")
            if self.CheckIfColor(textC):
                self.SimplifySetColor(guy, textC, "Text")
            if self.CheckIfColor(secondaryText):
                self.SimplifySetColor(guy, secondaryText, "SecondaryText")
            if self.CheckIfColor(outputBg):
                self.SimplifySetColor(guy, outputBg, "OutputBg")
            if self.CheckIfColor(outputText):
                self.SimplifySetColor(guy, outputText, "OutputText")
        if self.CheckIfColor(primary):
            self.GUI.our_window.configure(bg=primary)
            self.GUI.primary_color = primary
        if self.CheckIfColor(secondary):
            self.GUI.secondary_color = secondary
        if self.CheckIfColor(tertiary):
            self.GUI.tertiary_color = tertiary
        if self.CheckIfColor(textC):
            self.GUI.our_window.configure(highlightcolor=textC)
            self.GUI.text_color = textC
        if self.CheckIfColor(secondaryText):
            self.GUI.secondary_text_color = secondaryText
        if self.CheckIfColor(outputBg):
            self.GUI.output_bg = outputBg
        if self.CheckIfColor(outputText):
            self.GUI.output_text = outputText

    def SimplifySetColor(self, guy, color, type_guy):
        try:
            if guy[1] == type_guy:
                guy[0].configure(background=color)
            if guy[2] == type_guy:
                guy[0].configure(foreground=color)
        except Exception:
            pass


    def CheckIfColor(self, our_color):
        if our_color is None:
            return False
        else:
            return True
