# Text Editor - Notepad style application that can open, edit, and save text
# documents. Optional: Add syntax highlighting and other features.

from tkinter import * # Module used for creating GUI
import tkinter.scrolledtext as tkst

#Temporary function for different commands
def doNothing():
    print('do nothing function')
 
# Creates the window & title
window = Tk()
window.title('Text Editor')

# Creates a toolbar
menuBar = Menu(master=window)
window.config(menu=menuBar)

# Creating File submenu
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=doNothing)
fileMenu.add_command(label='Open', command=doNothing)
fileMenu.add_command(label='Save', command=doNothing)
fileMenu.add_command(label='Save as...', command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=doNothing)

# Creating Edit submenu
editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Cut', command=doNothing)
editMenu.add_command(label='Copy', command=doNothing)
editMenu.add_command(label='Paste', command=doNothing)
editMenu.add_command(label='Delete', command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Select All', command=doNothing)

# Creating text window & scrollbar
textBox = tkst.ScrolledText(window, wrap=WORD)
textBox.pack(fill=BOTH, expand=1)

# Keeps the window from closing
window.mainloop()