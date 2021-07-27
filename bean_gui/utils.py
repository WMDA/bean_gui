import tkinter as tk

class TextRedirect:
    '''
    Class to redirect stdout to widget
    '''
    def __init__(self,widget):
        self.widget = widget

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str)
        self.widget.configure(state="disabled")