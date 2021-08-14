import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pandas as pd


global_data = {}

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filepath:
        return

    data = pd.read_csv(filepath)

    global_data['data1'] = data

    label['text'] = filepath
    btn_clear['state'] = tk.NORMAL

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    global_data["data1"].to_csv(filepath)

def clear_screen():
    label.master.destroy()
    btn_clear['state'] = tk.DISABLED

def hover(event):
    l = tk.Label()
    df = global_data["data1"]

    dims = df.shape

    info_text = f"The number of rows is {dims[0]} and the number of columns is {dims[1]}"
    messagebox.showinfo("Title", info_text)



window = tk.Tk()
window.title("Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Load data", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_clear = tk.Button(fr_buttons, text="clear", command=clear_screen, state=tk.DISABLED)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_clear.grid(row=2, column=0, sticky="ew", padx=5)

editor = tk.Frame(window)
label = tk.Label(editor, text="example", relief=tk.RAISED)
label.grid(row=0, column=1, sticky="ns", padx=15, pady=15)

label.bind("<Enter>", hover)

fr_buttons.grid(row=0, column=0, sticky="ns")
editor.grid(row=0, column=1, sticky="nsew")

window.mainloop()