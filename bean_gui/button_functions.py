import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import sys
import pandas as pd
from utils import StdoutRedirect, set_style

class DisplayButton:

    '''
    Class to create a display button that when clicks opens a file finder. Finds csvs and prints the csv to a widget.

    Parameters
    ----------
    root : tk.TK() object
    widget : tk.widget object

    Return
    ------
    Widget button that opens file finder.
    
    '''

    def __init__(self,root,widget):
        self.window_button=ttk.Button(root,text='Open_data',command=self.import_data)
        self.style=set_style(self.window_button)
        sys.stdout = StdoutRedirect(widget)
        self.window_button.pack()

        
    def import_data(self):
        file=askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv","*.csv"),("all files","*.*")))
        self.df=pd.read_csv(file)
        print(self.df)
    

def load_web_page(url):
    
    '''
    Loads webpage

    Parameters
    ----------
    url: str, url of website to open

    Returns
    -------
    Website in default browser
    '''
    import webbrowser
    webbrowser.open(url)

def open_new_window(root,window,size='Full_screen'):

    '''
    Opens a new window destroying the old one.

    Parameters
    ----------
    root: tk.Tk() object
    window: A window object to open.
    size: turple int, optional. 

    Returns
    -------
    window object
    '''
    root.withdraw()
    root.destroy()
    window(size)
