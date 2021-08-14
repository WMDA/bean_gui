import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import ttk
from utils import current_size, window_size, set_style
from button_functions import load_web_page

class Window:
    
    '''
    Base class for Bean windows.
    
    Usage:
    from windows import Window

    Window(root,size=(2,3))

    Parameters
    --------------------------------
    size: turple int optional. 
    Default behaviour is full screen

    Returns 
    --------------------------------
    
    Window Class
    '''

    def __init__(self, size='Full_screen'):
        root_intialiser=self.root_window(size)
        style=set_style(self.root)
        file_button=self.menu(self.root)
        window_frame=self.window(self.root,self.w_size['height'],self.w_size['width'])
        self.root.mainloop()
        
    def root_window(self,size):
        self.root=tk.Tk()
        self.root.overrideredirect(True)
        self.winsize=current_size(self.root)
        self.w_size=window_size(self.root,size)
        title_bar = ttk.Frame(self.root)
        text=ttk.Label(title_bar,text='BEAN',padding=3,justify='center')
        close_button = ttk.Button(title_bar, text='X', command=self.root.destroy,cursor='hand1', width=3)
        max=ttk.Button(title_bar, text='□', command=self.max_window,cursor='hand1', width=3)
        min=ttk.Button(title_bar, text='-', command=self.min_window,cursor='hand1', width=3)
        title_bar.pack(fill=tk.X,side=tk.TOP)
        close_button.pack(side=tk.RIGHT)
        max.pack(side=tk.RIGHT)
        min.pack(side=tk.RIGHT)
        text.pack(side=tk.BOTTOM)
        title_bar.bind('<B1-Motion>', self.move_window)
        self.root.geometry(f"{int(self.w_size['width'])}x{int(self.w_size['height'])}")

    def min_window(self):
        self.root.geometry(f"{int(self.winsize['width']/2)}x{int(self.winsize['height']/2)}")
        
    def max_window(self):
        self.root.geometry(f"{int(self.winsize['width'])}x{int(self.winsize['height'])}")
       
    def window(self,root,height,width):
        self.frame=tk.Frame(root,height=height,width=width,bg='grey10')
        self.frame.pack(fill=tk.BOTH,expand=True)

    def move_window(self,event):
           self.root.geometry(f'+{event.x_root}+{event.y_root}')
    
    def menu(self,root):
        menu=tk.Frame(root,bg='purple4')
        menu.pack(fill=tk.BOTH)
        
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


class Landing_page(Window):
    def __init__(self, size='Full_screen'):
        root_intialiser=self.root_window(size)
        style=set_style(self.root)
        self.window_frame=self.window(self.root,self.w_size['height'],self.w_size['width'])
        self.bar_frame=ttk.Frame(self.frame)
        self.bar_frame.pack(side=tk.LEFT,fill=tk.Y)
        buttons=self.buttons()
        self.root.mainloop()


    def buttons(self):
        data=ttk.Button(self.bar_frame,cursor='hand1',text='Open Data',padding=10)
        new_bean_project=ttk.Button(self.bar_frame,cursor='hand1',text='New Bean Project',padding=10)
        old_bean_project=ttk.Button(self.bar_frame,cursor='hand1',text='Open BEAN project',padding=10)
        help=ttk.Button(self.bar_frame,cursor='hand1',text='Help',padding=10,command=lambda: load_web_page('https://github.com/WMDA/bean_gui'))
        contribute=ttk.Button(self.bar_frame,cursor='hand1',text='Contribute',padding=10, command=lambda: load_web_page('https://github.com/WMDA/bean_gui'))
        credit=ttk.Button(self.bar_frame,cursor='hand1',text='Credits',padding=10)
        close=ttk.Button(self.bar_frame,cursor='hand1',text='Close',padding=10,command=self.root.destroy)


        data.pack(side=tk.TOP,expand=True) 
        new_bean_project.pack(side=tk.TOP,expand=True)
        old_bean_project.pack(side=tk.TOP,expand=True)
        help.pack(side=tk.TOP,expand=True)
        credit.pack(side=tk.TOP,expand=True)
        contribute.pack(side=tk.TOP,expand=True)
        close.pack(side=tk.TOP,expand=True)

        