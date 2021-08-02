import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import ttk
from utils import window_size, set_style

class Window:
    
    '''
    Base class for window.
    
    Usage:
    from windows import Window
    import tkinter as tk

    root=tk.Tk()
    Window(root,size=(2,3))

    Parameters
    ----------------------
    root: tk.Tk() object
    size: turple int optional. Default behaviour is the full screen

    Returns 
    '''

    def __init__(self,root,size='Full_screen'):
        self.style=set_style(root)
        self.window_frame=self.window(root,size)
        
    def window(self,root,size):
        w_size=window_size(root,size)
        frame=ttk.Frame(master=root,width=w_size['width'], height=w_size['height'])
        frame.pack(fill=tk.BOTH,expand=True)