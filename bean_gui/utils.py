import tkinter as tk
from tkinter import ttk
import os

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

def window_size(root,size='Full_screen'):
    
    '''
    Function to resize window. Default is
    full screen. Takes a turple that that divides width 
    and height by to produce new window dimentions
    
    Parameters
    -----------
    root : Tk() object
    size : turple of two int , optional 
         First element is int to divde width by 
         second elment is int to divide height by

    Returns
    ----------
    Dictionary of width and value dimensions 

    '''

    if size =='Full_screen':
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        spec={'width':width ,'height':height}
        return spec
    else:
        width = root.winfo_screenwidth() /size[0]
        height = root.winfo_screenheight()/size[1]
        spec={'width':width ,'height':height}
        return spec
    
def set_style(root,style='awdark'):
    ttk_style=style
    '''
    Function to set style. Default is
    awdark. 
    
    Parameters
    -----------
    root : Tk() object
    size : str optional
        sets style
    Returns
    ----------
    style  

    '''
    os.chdir("..")
    styles_path = os.path.abspath('styles')
    style = ttk.Style(root)
    root.tk.eval(f"""set base_theme_dir {styles_path}/awthemes-10.4.0
    package ifneeded awthemes 10.4.0 \
    [list source [file join $base_theme_dir awthemes.tcl]]
    package ifneeded colorutils 4.8 \
    [list source [file join $base_theme_dir colorutils.tcl]]
    package ifneeded {ttk_style} 7.12 \
    [list source [file join $base_theme_dir {ttk_style}.tcl]]
    """)
    root.tk.call("package", "require", ttk_style)
    return style.theme_use(ttk_style)