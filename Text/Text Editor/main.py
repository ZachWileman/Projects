# Text Editor - Notepad style application that can open, edit, and save text
# documents. Optional: Add syntax highlighting and other features.

from tkinter import * # Module used for creating GUI
import tkinter.scrolledtext as tkst
from tkinter.filedialog import askopenfilename
import sys

#Temporary function for different commands
def doNothing():
    print('do nothing function')

# Exit function
def exitProgram():
    # *********************Need to add check for if user wants to save file
    pass

# Open file function
def openFile():
    fileName = askopenfilename(
        filetypes=[('All Files', '*.*')],
        title = 'Choose A File'
        )

    # SIDE-NOTE: 'end-1c' refers to one character back from END. END points to
    # just beyond the last character in the text string, this expression refers
    # to the last character itself. The -1c extension effectively strips the
    # trailing \n that this widget adds to its contents (and which may add a
    # blank line if saved in a file). Source: [O`Reilly] - Programming Python,
    # 4th ed. For this function, END+'-1c' or 'end-1c' do the same thing.
    if len(textBox.get('1.0', 'end-1c')):
        textBox.delete('1.0', END)
        #*********** Need to add check for if there is a file open before it
        #*********** clears the text editor.

    if fileName:
        try:
            with open(fileName) as f:
                contents = f.read()
                textBox.insert('1.0', contents)
        except:
            print('An error occured when trying to open the file.')
 
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
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=doNothing)
fileMenu.add_command(label='Save as...', command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=exitProgram)

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