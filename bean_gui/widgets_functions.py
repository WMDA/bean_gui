import tkinter as tk
import os
import sys
import pandas as pd
from utils import TextRedirect

class DisplayButton:
    def __init__(self,root,widget):
        self.window_button=tk.Button(root,text='Open_data',command=self.import_data)
        sys.stdout = TextRedirect(widget)
        self.window_button.pack()

        
    def import_data(self):
        file=tkf.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv","*.csv"),("all files","*.*")))
        self.df=pd.read_csv(file)
        print(self.df)

