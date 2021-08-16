from tkinter import ttk
import os

class StdoutRedirect:
    '''
    Class used to redirect stdout to widget. 
    Used with widgets that accept text

    Usage:

    import sys
    sys.stdout=TextRedirect(widget)

    Parameters
    -----------------------
    widget : tk.widget object

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
    full screen. Takes a turple that divides width 
    and height by to produce new window dimentions
    
    Parameters
    -----------
    root : tk object, window
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
    else:
        width = root.winfo_screenwidth() /size[0]
        height = root.winfo_screenheight()/size[1]
    spec={'width':int(width) ,'height':int(height)}
    return spec

def current_size(root):
     
    '''
    Function to get window size.
    
    Parameters
    -----------
    root : tk object, window

    Returns
    ----------
    Dictionary of width and value dimensions 

    '''

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    size={'width':width ,'height':height}
    return size
    
def set_style(root,style='awdark'):
    
    '''
    Function to set style. Default is
    awdark. 
    
    Parameters
    -----------
    root : Tk() object
    style: str optional. Default is awdark

    Returns
    ----------
    style  

    '''
    ttk_style=style
    location=os.getcwd()
    if '/bean_gui/' in location:
        os.chdir('..')
    styles_path = os.path.abspath('styles') #todo find a more robust way to find the 'styles' folder. currently only works if in bean_gui directory
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