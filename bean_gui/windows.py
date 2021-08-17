import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import ttk
from utils import current_size, window_size, set_style
from button_functions import load_web_page, open_new_window

class Window:
    
    '''
    Base class for Bean windows.
    
    Usage:
    from windows import Window

    Window(root,size=(2,3))

    Parameters
    ----------
    size: turple int optional. 
          Default behaviour is full screen

    Returns 
    -------
    
    Window Class
    '''

    def __init__(self, size='Full_screen'):
        self.root_intialiser=self.root_window(size)
        self.style=set_style(self.root)
        self.file_button=self.menu(self.root)
        self.window_frame=self.window(self.root,self.w_size['height'],self.w_size['width'])
        self.root.mainloop()
        
    def root_window(self,size):

        '''
        Function to create customise root window. BEAN has own title bar with close button, min and max buttons. This is to reduce variation across 
        os and gives BEAN a disinct look and feel.

        Parameters
        ----------
        self: self parameter
        size: turple int optional. 
              Default behaviour is full screen
        
        Returns
        -------
        Customised root window (a tk.Tk() object) 
        '''

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
        self.root.geometry(f"{self.w_size['width']}x{self.w_size['height']}") #todo create ability to drag and resize root window

    def min_window(self): #todo create a minimize button to minimize screen to titel bar
        self.root.geometry(f"{int(self.winsize['width']/2)}x{int(self.winsize['height']/2)}")
        
    def max_window(self):
        self.root.geometry(f"{self.winsize['width']}x{self.winsize['height']}")
       
    def window(self,root,height,width):
        self.frame=tk.Frame(root,height=height,width=width,bg='grey10')
        self.frame.pack(fill=tk.BOTH,expand=True)

    def move_window(self,event):
           self.root.geometry(f'+{event.x_root}+{event.y_root}')
    
    def menu(self,root):

        '''
        Function to create a menu bar. Includes File, view and help button.

        Parameters
        ----------
        self: self
        root: tk.Tk() object

        Returns
        -------
        Frame for Menu
        '''

        menu=tk.Frame(root,bg='purple4')
        menu.pack(fill=tk.BOTH)
        
        #File button
        file_button=ttk.Menubutton(menu,text='File',cursor='hand1')
        tkmenu=tk.Menu(file_button)
        file_menu=tk.Menu(tkmenu,tearoff=0,background='grey16',foreground='white')
        file_menu.add_separator()
        file_menu.add_command(label='Open Data')
        file_menu.add_command(label='New Bean file',command=lambda:open_new_window(self.root,Block_window))
        file_menu.add_command(label='Open Bean file')
        file_menu.add_command(label='Credits')
        file_menu.add_command(label='Contribute',command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui')))
        file_menu.add_command(label='Back to Main Page',command=lambda:open_new_window(self.root,Landing_page))
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
        help_menu.add_command(label='Help',command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui')))
        help_menu.add_command(label='Report bug',command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui/issues')))
        help_menu.add_separator()
        help_button["menu"] = help_menu
        help_button.pack(side=tk.LEFT)


class Landing_page(Window):

    '''
    Opening window for BEAN. Inherents functionality from  Windows base class minus menu bar
    
    Usage:
    from windows import Window

    Window(size=(2,3))

    Parameters
    ----------
    size: turple int optional. 
          Default behaviour is full screen

    Returns 
    -------
    
    Opening page Class
    '''

    def __init__(self, size='Full_screen'):
        self.root_intialiser=self.root_window(size)
        self.style=set_style(self.root)
        self.window_frame=self.window(self.root,self.w_size['height'],self.w_size['width'])
        self.side_buttons=self.bar()
        self.root.mainloop()


    def bar(self):

        '''
        Function to create side bar with functional buttons, load data
        open bean project, new bean project, help, report a bug and close.

        Parameters
        ----------
        self: self parameter

        Returns
        -------
        Side bar with functional buttons
        '''
        bar_frame=ttk.Frame(self.frame)
        bar_frame.pack(side=tk.LEFT,fill=tk.Y)

        data=ttk.Button(bar_frame,cursor='hand1',text='Open Data',padding=10,command=lambda:open_new_window(self.root,Window))
        data.pack(side=tk.TOP,expand=True,padx=5) 

        new_bean_project=ttk.Button(bar_frame,cursor='hand1',text='New Bean Project',padding=10,command=lambda:open_new_window(self.root,Block_window))
        new_bean_project.pack(side=tk.TOP,expand=True,padx=5)

        old_bean_project=ttk.Button(bar_frame,cursor='hand1',text='Open BEAN project',padding=10)
        old_bean_project.pack(side=tk.TOP,expand=True,padx=5)

        help=ttk.Button(bar_frame,cursor='hand1',text='Help',padding=10,command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui')))
        help.pack(side=tk.TOP,expand=True,padx=5)

        contribute=ttk.Button(bar_frame,cursor='hand1',text='Contribute',padding=10, command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui')))
        contribute.pack(side=tk.TOP,expand=True,padx=5)

        report=ttk.Button(bar_frame,cursor='hand1',text='Report an issue',padding=10, command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui/issues')))
        report.pack(side=tk.TOP, expand=True,padx=5)

        credit=ttk.Button(bar_frame,cursor='hand1',text='Credits',padding=10)
        credit.pack(side=tk.TOP,expand=True,padx=5)

        close=ttk.Button(bar_frame,cursor='hand1',text='Close',padding=10,command=self.root.destroy)
        close.pack(side=tk.TOP,expand=True,padx=5)

class Block_window(Window):

    '''
    Main BEAN page. Creates block to be used to chain statistical tests together.

    Inherents functionality from Windows base
    
    Usage:
    from windows import Block_window

    Block_window(size=(2,3))

    Parameters
    ----------
    size: turple int optional. 
          Default behaviour is full screen

    Returns 
    -------
    
    Block window
    '''

    def __init__(self, size='Full_screen'):
        self.root_intialiser=self.root_window(size)
        self.style=set_style(self.root)
        self.file_button=self.menu(self.root)
        self.window_frame=self.window(self.root,self.w_size['height'],self.w_size['width'])
        self.side_buttons=self.bar()     
        self.root.mainloop()
    
    def bar(self):
        
        #Creates frame to use as basis for bar
        bar_frame=ttk.Frame(self.frame)
        bar_frame.pack(side=tk.RIGHT,fill=tk.Y)

        #Creates an add and delete button
        add_dataset=ttk.Button(bar_frame,cursor='hand1',text='Add Block',padding=10,command=lambda:self.block('Block'))
        add_dataset.pack(side=tk.TOP, expand=True)
        
        delete_test_block=ttk.Button(bar_frame,cursor='hand1',text='Delete',padding=10,command=self.delete)
        delete_test_block.pack(side=tk.BOTTOM,expand=True)

    def block(self,txt):
        self.label=tk.Label(self.frame,text=txt,height=5, width=10,bg='purple4',fg='black',cursor='plus',font='14')
        self.label.pack(expand=True,side=tk.TOP)
        self.drag_and_drop(self.label) #todo stop blocks from being able to be placed on side bar
        self.click(self.label)

    def delete(self): #todo this function currently doesn't work.
        self.label.destroy

    def drag_and_drop(self,widget):
        widget.bind("<Button-1>", self.start_dragging)
        widget.bind("<B1-Motion>", self.dragging)

    def start_dragging(self,event):
        event.widget._drag_start_x = event.x
        event.widget._drag_start_y = event.y
        
    def dragging(self,event):
        x = event.widget.winfo_x() - event.widget._drag_start_x + event.x
        y = event.widget.winfo_y() - event.widget._drag_start_y + event.y
        event.widget.place(x=x, y=y)

    def click(self,widget):
        widget.bind("<Double-1>", self.define_block)

    def define_block(self,event):
        Define_block()

class Define_block(Window):
    def __init__(self, size=(2,1)):
        self.root_intialiser=self.root_window(size)
        self.style=set_style(self.root)
        self.window_frame=self.window(self.root,self.w_size['height'],self.w_size['width'])   
        self.root.mainloop()
