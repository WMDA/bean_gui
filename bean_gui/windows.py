import tkinter as tk #Due to numerous imports importing as tkinter as tk allows to keep track what is from tkinter and what isn't
from tkinter import Widget, ttk, scrolledtext
import tkinter
from utils import current_size, window_size, set_style
from button_functions import load_web_page, open_new_window
import pandas as pd

class Base_window:
    
    '''
    Base class for Bean windows. 
    Not useable as doesn't have mainloop feature

    Parameters
    --------------------------------
    size: turple int optional. 
    Default behaviour is full screen

    Returns 
    --------------------------------
    
    Window Class
    '''

    def __init__(self, size='Full_screen',window_type='Base'):
        self.root_intialiser=self.root_window(size)
        self.style=set_style(self.root)
        if window_type=='Base':
            self.file_button=self.menu(self.root)
        self.window_frame=self.window(self.root,self.w_size['height'],self.w_size['width'])
        
        
    def root_window(self,size):
        '''
        Function to create customise root window.
        BEAN has own title bar with close button, min
        and max buttons. This is to reduce variation across 
        os and gives BEAN a disinct look and feel.

        Parameters
        ---------------------------------------------------
        self: self parameter
        size: turple int optional. 
        Default behaviour is full screen
        
        Returns
        ---------------------------------------------------
        Customised root window (a tk.Tk() object) 
        '''

        self.root=tk.Tk()
        #self.root.overrideredirect(True)
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
        self.root.geometry(f"{self.w_size['width']}x{self.w_size['height']}")

    def min_window(self):
        self.root.geometry(f"{int(self.winsize['width']/2)}x{int(self.winsize['height']/2)}")
        
    def max_window(self):
        self.root.geometry(f"{self.winsize['width']}x{self.winsize['height']}")
       
    def window(self,root,height,width):
        self.frame=tk.Frame(root,height=height,width=width,bg='grey10')
        self.frame.pack(fill=tk.BOTH,expand=True)

    def move_window(self,event):
           self.root.geometry(f'+{event.x_root}+{event.y_root}')
    
    def menu(self, root):
        '''
        Function to create a menu bar.
        Includes File, view and help button.

        Parameters
        ------------------------------------
        self: self
        root: tk.Tk() object
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

class Window(Base_window):
    def __init__(self, size='Full_size',window_type='Base'):
        super().__init__(size=size,window_type=window_type)
        self.root.mainloop()

class Landing_page(Base_window):

    '''
    Opening window for BEAN. 
    Inherents functionality from 
    Windows base class minus menu bar
    
    Usage:
    from windows import Window

    Window(size=(2,3))

    Parameters
    --------------------------------
    size: turple int optional. 
    Default behaviour is full screen

    Returns 
    --------------------------------
    
    Opening page Class
    '''

    def __init__(self, size='Full_screen',window_type='Landing'):
        super().__init__(size=size,window_type=window_type)
        self.side_buttons=self.buttons()
        self.root.mainloop()


    def buttons(self):
        bar_frame=ttk.Frame(self.frame)
        bar_frame.pack(side=tk.LEFT,fill=tk.Y)

        button_config = {
            'master' : bar_frame,
            'padding': 10,
            'cursor': 'hand1'

        }
        left_buttons = []
        left_buttons.append(ttk.Button(**button_config, text='Open Data', command=lambda:open_new_window(self.root,Window)) )
        left_buttons.append(ttk.Button(**button_config, text='New Bean Project',command=lambda:open_new_window(self.root,Block_window)) )
        left_buttons.append(ttk.Button(**button_config, text='Open BEAN project') )
        left_buttons.append(ttk.Button(**button_config, text='Help', command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui'))) )
        left_buttons.append(ttk.Button(**button_config, text='Contribute', command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui'))) )
        left_buttons.append(ttk.Button(**button_config, text='Report an issue', command=lambda: (self.min_window(),load_web_page('https://github.com/WMDA/bean_gui/issues'))) )
        left_buttons.append(ttk.Button(**button_config, text='Credits') )
        left_buttons.append(ttk.Button(**button_config, text='Close', command=self.root.destroy) )

        for button in left_buttons:
            button.pack(side=tk.TOP, expand=True, padx=5) 

class Block_window(Base_window):

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

    def __init__(self, size='Full_screen',window_type='Base'):
        super().__init__(size=size,window_type=window_type)
        self.side_buttons=self.bar()     

    def bar(self):
        
        #Creates frame to use as basis for bar
        bar_frame=ttk.Frame(self.frame)
        bar_frame.pack(side=tk.RIGHT,fill=tk.Y)

        bar_config = {
            'master': bar_frame,
            'cursor': 'hand1',
            'padding': 10
        }
        #Creates an add and delete button
        create_block = ttk.Button(**bar_config, text='Add Block', command= lambda:CreateBlock(self.root) )
        create_block.pack(side=tk.TOP, expand=True)

        load_bean=ttk.Button(**bar_config, text='Load Bean Project')
        load_bean.pack(side=tk.TOP, expand=True)

        back=ttk.Button(**bar_config, text='Back to main page', command=lambda:open_new_window(self.root,Landing_page))
        back.pack(side=tk.TOP, expand=True)
        
    def block(self,txt):
        self.label=tk.Label(self.frame,text=txt,height=5, width=10,bg='purple4',fg='black',cursor='plus',font='14')
        self.label.pack(expand=True,side=tk.TOP)
        self.block_functions(self.label)
        
    def block_functions(self,widget): #The event parameter makes this difficult to make into a class that can be imported. Currently works as nested functions 

        def start_dragging(event):
            event.widget._drag_start_x = event.x
            event.widget._drag_start_y = event.y
        
        def dragging(event):
            x = event.widget.winfo_x() - event.widget._drag_start_x + event.x
            y = event.widget.winfo_y() - event.widget._drag_start_y + event.y
            event.widget.place(x=x, y=y)

        def define_block(event):
            Define_block(self.root)
 
        def hover(event):
            self.hover_box=ttk.Label(self.frame,text='Left click to drag \nDouble click to define block \nRight click to delete',font=(14))
            self.hover_box.pack(side=tk.BOTTOM)
        
        def exit(event):
            self.hover_box.destroy()
        
        def delete_function(event):
            self.hover_box.destroy()
            self.label.destroy()
        
        widget.bind("<Double-1>", define_block)
        widget.bind("<Button-3>", delete_function)
        widget.bind("<Button-1>", start_dragging)
        widget.bind("<B1-Motion>",dragging)  #todo stop blocks from being able to be placed on side bar
        widget.bind("<Enter>",hover)
        widget.bind("<Leave>",exit)

class Define_block(Window):
    def __init__(self,root):
        root=root
        window_top=tk.Toplevel()
        w_size=window_size(window_top,size=(3,3))
        window_top.geometry(f"{w_size['width']}x{w_size['height']}")
        window=ttk.Frame(window_top)
        window.pack(fill=tk.BOTH,expand=True,side=tk.TOP)
        window.lift()
        block_type=ttk.Combobox(window,values=('Dataset, statistical Test, Graph'))
        block_type.pack(side=tk.TOP)
        window_top.mainloop()

class CreateBlock(Window):
    def __init__(self,root):
        root=root
        window_top=tk.Toplevel()
        w_size=window_size(window_top,size=(3,3))
        window_top.geometry(f"{w_size['width']}x{w_size['height']}")
        window=ttk.Frame(window_top)
        window.pack(fill=tk.BOTH,expand=True,side=tk.TOP)
        window.lift()

        tab_control = ttk.Notebook(window)

        # data tab
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Load Data')
        lbl1 = ttk.Button(tab1, text="choose data", command= lambda:choose_data())
        lbl1.grid(column=0, row=0)

        txt = scrolledtext.ScrolledText(tab1,width=40,height=10)
        txt.grid(column=0,row=1)

        # stats tab
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Stats')
        lbl2 = ttk.Label(tab2, text= 'label2')
        lbl2.grid(column=0, row=0)

        tab_control.pack(expand=1, fill='both')

        def choose_data():
            file = tk.filedialog.askopenfilename(filetypes = ((".csv","*.csv"),("all files","*.*")))   
            if '.csv' not in file:
                print("only csv bitch!")
            data = pd.read_csv(file)
            txt.insert(tk.INSERT, f'The number of rows is {data.shape[0]} \n The number of columns is {data.shape[1]} ')


            
            
