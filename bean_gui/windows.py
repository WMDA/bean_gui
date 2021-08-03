import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import ttk
from utils import window_size, set_style

class Window:
    
    '''
    Base class for Bean windows.
    
    Usage:
    from windows import Window
    import tkinter as tk

    root=tk.Tk()
    Window(root,size=(2,3))

    Parameters
    ----------------------
    root: tk.Tk() object
    size: turple int optional. Default behaviour is full screen

    Returns 
    -----------------------
    Window Class
    '''

    def __init__(self,root,size='Full_screen'):
        self.style=set_style(root)
        self.file_button=self.menu(root)
        self.window_frame=self.window(root,size)
        
        
    def window(self,root,size):
        w_size=window_size(root,size)
        frame=ttk.Frame(master=root,width=w_size['width'], height=w_size['height'],cursor='hand1')
        frame.pack(fill=tk.BOTH,expand=True)
    
    def menu(self,root):
        self.menu_bar=tk.Menu(root, activebackground='green',tearoff=0,bg='purple',fg='black')
        
        #File button
        self.file_button=tk.Menu(self.menu_bar,tearoff=0,background='black',foreground='white')
        self.file_button.add_command(label='Open Data')
        self.file_button.add_cascade(label='Open Bean file')
        self.file_button.add_command(label='Close',command=root.destroy)
        self.menu_bar.add_cascade(label='File',menu=self.file_button)
        self.file_button.add_separator()

        #View button
        self.help_button=tk.Menu(self.menu_bar,tearoff=0,background='black',foreground='white')
        self.help_button.add_command(label='View Source Code')
        self.help_button.add_command(label='View Markdown')
        self.menu_bar.add_cascade(label='View',menu=self.help_button)
        self.help_button.add_separator()

        #Help button
        self.help_button=tk.Menu(self.menu_bar,tearoff=0,background='black',foreground='white')
        self.help_button.add_command(label='Help')
        self.menu_bar.add_cascade(label='Help',menu=self.help_button)
        self.help_button.add_separator()

        root.config(menu=self.menu_bar)
      