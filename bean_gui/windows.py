import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import ttk
from utils import current_size, window_size, set_style

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
        root_intialiser=self.root_window(size)
        root=self.root
        w_size=window_size(root,size)
        self.root.geometry(f"{int(w_size['width'])}x{int(w_size['height'])}")
        style=set_style(root)
        file_button=self.menu(root)
        window_frame=self.window(root,w_size['height'],w_size['width'])
        root.mainloop()
        
    def root_window(self,size):
        self.root=tk.Tk()
        self.root.overrideredirect(True)
        self.winsize=current_size(self.root)
        self.check=window_size(self.root,size)
        title_bar = ttk.Frame(self.root)
        text=ttk.Label(title_bar,text='BEAN',padding=3)
        close_button = ttk.Button(title_bar, text='X', command=self.root.destroy,cursor='hand1', width=3)
        resize=ttk.Button(title_bar, text='□', command=self.resize_window,cursor='hand1', width=3)
        title_bar.pack(fill=tk.X,side=tk.TOP,expand=True)
        close_button.pack(side=tk.RIGHT)
        resize.pack(side=tk.RIGHT)
        text.pack(side=tk.BOTTOM)
        title_bar.bind('<B1-Motion>', self.move_window)
        self.root.resizable(True, True)

    def resize_window(self):
        if (self.check['width'] and self.check['height'])==(self.winsize['width'] and self.winsize['height']):
            self.root.geometry(f"{int(self.winsize['width']/2)}x{int(self.winsize['height']/2)}")
        else:
            self.root.geometry(f"{int(self.winsize['width'])}x{int(self.winsize['height'])}")
       
    def window(self,root,height,width):
        self.frame=tk.Frame(root,height=height,width=width,bg='grey10')
        self.frame.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)

    def move_window(self,event):
           self.root.geometry(f'+{event.x_root}+{event.y_root}')
    
    def menu(self,root):
        menu=tk.Frame(root,bg='purple4')
        menu.pack(fill=tk.BOTH,expand=True)
        
        #File button
        file_button=ttk.Menubutton(menu,text='File',cursor='hand1')
        tkmenu=tk.Menu(file_button)
        file_menu=tk.Menu(tkmenu,tearoff=0,background='grey16',foreground='white')
        file_menu.add_separator()
        file_menu.add_command(label='Open Data')
        file_menu.add_command(label='Open Bean file')
        file_menu.add_command(label='Close',command=self.root.destroy)
        file_menu.add_separator()
        file_button["menu"] = file_menu
        file_button.pack(side=tk.LEFT)
        
        #View button
        view_button=ttk.Menubutton(menu,text='View',cursor='hand1')
        view_menu=tk.Menu(tkmenu,tearoff=0,background='grey16',foreground='white')
        view_menu.add_separator()
        view_menu.add_command(label='View Source Code')
        view_menu.add_command(label='View Markdown')
        view_menu.add_separator()
        view_button["menu"] = view_menu
        view_button.pack(side=tk.LEFT)

        #Help button
        help_button=ttk.Menubutton(menu,text='Help',cursor='hand1')
        help_menu=tk.Menu(tkmenu,tearoff=0,background='grey16',foreground='white')
        help_menu.add_separator()
        help_menu.add_command(label='Help')
        help_menu.add_separator()
        help_button["menu"] = help_menu
        help_button.pack(side=tk.LEFT)