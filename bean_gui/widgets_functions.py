import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter.filedialog import askopenfilename
import os
import sys
import pandas as pd
from utils import StdoutRedirect

class DisplayButton:

    '''
    Class to create a display button that when clicks opens a file finder. 
    Finds csvs and prints the csv to a widget.

    Parameters
    -------------------------------
    root : tk.TK() object
    widget : tk.widget object

    Return
    ------------------------------
    Widget button that opens file finder.
    '''

    def __init__(self,root,widget):
        self.window_button=tk.Button(root,text='Open_data',command=self.import_data)
        sys.stdout = StdoutRedirect(widget)
        self.window_button.pack()

        
    def import_data(self,root):
        file=askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv","*.csv"),("all files","*.*")))
        self.df=pd.read_csv(file)
        print(self.df)
    
        
