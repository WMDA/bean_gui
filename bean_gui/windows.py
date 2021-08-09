import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import ttk
from utils import get_window_size, window_size, set_style

class Window:
    
    '''
    Base class for Bean windows.
    
    Usage:
    from windows import Window

    Window(root,size=(2,3))

    Parameters
    ----------------------
    size: turple int optional. Default behaviour is full screen

    Returns 
    -----------------------
    Window Class
    '''

    def __init__(self, size='Full_screen'):
        root_intialiser=self.root_window()
        root=self.root
        w_size=window_size(root,size)
        self.root.geometry(f"{int(w_size['width'])}x{int(w_size['height'])}")
        style=set_style(root)
        file_button=self.menu(root)
        window_frame=self.window(root,w_size['height'],w_size['width'])
        root.mainloop()
        
    def root_window(self):
        self.root=tk.Tk()
        self.root.overrideredirect(True)
        title_bar = ttk.Frame(self.root)
        text=ttk.Label(title_bar,text='BEAN',padding=3)
        close_button = ttk.Button(title_bar, text='X', command=self.root.destroy,cursor='hand1', width=3)
        title_bar.pack(fill=tk.X,side=tk.TOP,expand=True)
        close_button.pack(side=tk.RIGHT)
        text.pack(side=tk.BOTTOM)
        title_bar.bind('<B2-Motion>', self.move_window)
    

    def window(self,root,height,width):
        self.frame=tk.Frame(root,height=height ,width=width,bg='Black')
        self.frame.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)

    def move_window(event):
           self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    
    def menu(self,root):
        menu=tk.Frame(root,bg='purple')
        menu.pack(fill=tk.BOTH,expand=True)
        
        #File button
        file_button=ttk.Menubutton(menu,text='File',cursor='hand1')
        file_menu=tk.Menu(file_button)
        file=tk.Menu(file_menu,tearoff=0,background='black',foreground='white')
        file.add_command(label='Open Data')
        file.add_command(label='Open Bean file')
        file.add_command(label='Close',command=self.root.destroy)
        file.add_separator()
        file_button["menu"] = file
        file_button.pack(side=tk.LEFT)
        
        #View button
        view_button=ttk.Menubutton(menu,text='View',cursor='hand1')
        view_menu=tk.Menu(file_menu,tearoff=0,background='black',foreground='white')
        view_menu.add_command(label='View Source Code')
        view_menu.add_command(label='View Markdown')
        view_menu.add_separator()
        view_button["menu"] = view_menu
        view_button.pack(side=tk.LEFT)

        #Help button
        help_button=ttk.Menubutton(menu,text='Help',cursor='hand1')
        help_menu=tk.Menu(file_menu,tearoff=0,background='black',foreground='white')
        help_menu.add_command(label='Help')
        help_menu.add_separator()
        help_button["menu"] = help_menu
        help_button.pack(side=tk.LEFT)