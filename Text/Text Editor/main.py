# Text Editor - Notepad style application that can open, edit, and save text
# documents. Optional: Add syntax highlighting and other features.

from tkinter import * # Module used for creating GUI

#Temporary function for different commands
def doNothing():
    print('do nothing function')

# Creates the window
window = Tk()

frame = Frame(window, width=300, height=300)
frame.pack()

# Creates a toolbar
menuBar = Menu(frame)
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

# Creating Scrollbar
scrollBar = Scrollbar(frame)
scrollBar.pack(side=RIGHT, fill=Y)

# Creating text window
text = Text(frame, wrap=WORD)
text.config(yscrollcommand=scrollBar.set)
text.pack(side=LEFT)

# Keeps the window from closing
window.mainloop()