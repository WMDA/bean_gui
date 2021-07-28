import tkinter as tk
from tkinter import ttk
from utils import window_size, set_style

class Window:
    def __init__(self,root,size='Full_screen'):
        self.style=set_style(root)
        self.window_frame=self.window(root,size)
        
    def window(self,root,size):
        w_size=window_size(root,size)
        frame=ttk.Frame(master=root,width=w_size['width'], height=w_size['height'])
        frame.pack(fill=tk.BOTH,expand=True)