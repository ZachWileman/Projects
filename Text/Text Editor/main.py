# Text Editor - Notepad style application that can open, edit, and save text
# documents. Optional: Add syntax highlighting and other features.

# Program developed using Python 3.4.4

from tkinter import * # Module used for creating GUI
import tkinter.scrolledtext as tkst
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askquestion, showerror
import sys

currentFile = ''

def selectAll(event=None):
    try:
        textBox.add_tag(SEL_FIRST, SEL_LAST)
    except:
        # Nothing to select
        pass

def undo(event=None):
    try:
        textBox.edit_undo()
    except:
        # Nothing to undo
        pass

def redo(event=None):
    try:
        textBox.edit_redo()
    except:
        # Nothing to redo
        pass

def deleteText(event=None):
    try:
        text = textBox.get(SEL_FIRST, SEL_LAST)
        textBox.delete(SEL_FIRST, SEL_LAST)
    except:
        pass

def cut(event=None):
    try:
        text = textBox.get(SEL_FIRST, SEL_LAST)
        textBox.delete(SEL_FIRST, SEL_LAST)
        window.clipboard_clear()
        window.clipboard_append(text)
    except:
        # Done to avoid errors in the console; not really necessary.
        pass

def copy(event=None):
    try:
        text = textBox.get(SEL_FIRST, SEL_LAST)
        window.clipboard_clear()
        window.clipboard_append(text)
    except:
        # Done to avoid errors in the console; not really necessary.
        pass

def paste(event=None):
    try:
        text = selection_get(selection='CLIPBOARD')
        textBox.insert(text)
    except:
        # Used for if the clipboard is empty
        pass

def newFile(event=None):
    global currentFile

    if textBox.edit_modified():
        choice = checkSave()

        if choice == 'yes':
            save()
            return
    
    textBox.delete('1.0', 'end-1c')
    currentFile = ''
    textBox.edit_modified(False)

def checkSave():
    global currentFile

    if currentFile:
        choice = askquestion('Text Editor', 'Do you want to save changes to ' +
                             currentFile + '?')
    else:
        choice = askquestion('Text Editor', 'Do you want to save changes to' +
                             ' Untitled?')
    return choice

# Exit function
def exitProgram():
    if textBox.edit_modified():
        choice = checkSave()

        if choice == 'yes':
            save()

    sys.exit()

# Used for saving to a new file (or optionally the same file)
def saveAs(event=None):
    fileName = asksaveasfilename()

    if fileName:
        contents = textBox.get('1.0', 'end-1c')
        try:
            with open(fileName, 'w') as f:
                f.write(contents)
            textBox.edit_modified(False)
        except:
            showerror('Error!', 'Unable to open file.')

# Save the current file
def save(event=None):
    global currentFile

    if currentFile:
        contents = textBox.get('1.0', 'end-1c')
        try:
            with open(currentFile, 'w') as f:
                f.write(contents)
            textBox.edit_modified(False)
        except:
            showerror('Error!', 'Unable to open file.')
    else:
        saveAs()

# Open file function
def openFile(event=None):
    global currentFile

    if textBox.edit_modified():
        choice = checkSave()

        if choice == 'yes':
            save()
            return

    fileName = askopenfilename(
        filetypes=[('All Files', '*.*')],
        title = 'Choose A File'
        )

    # SIDE-NOTE: 'end-1c' refers to one character back from END. END points to
    # just beyond the last character in the text string, this expression refers
    # to the last character itself. The -1c extension effectively strips the
    # trailing \n that this widget adds to its contents (and which may add a
    # blank line if saved in a file). Source: [O`Reilly] - Programming Python,
    # 4th ed. For this function(below), END+'-1c' or 'end-1c' do the same thing.

    if fileName:
        textBox.delete('1.0', 'end-1c')

        try:
            with open(fileName) as f:
                contents = f.read()
                textBox.insert('1.0', contents)
            currentFile = fileName
            textBox.edit_modified(False)
        except:
            currentFile = ''
            showerror('Error!', 'Unable to open file.')
 
# Creates the window & title
window = Tk()
window.title('Text Editor')

# Creates a toolbar
menuBar = Menu(window)
window.config(menu=menuBar)

# Creating File submenu
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=newFile, accelerator='Ctrl+N')
fileMenu.add_command(label='Open', command=openFile, accelerator='Ctrl+O')
fileMenu.add_command(label='Save', command=save, accelerator='Ctrl+S')
fileMenu.add_command(label='Save as...', command=saveAs, 
                     accelerator='Ctrl+Shift+S')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=exitProgram)

# Adding protocol for if user hits the close button in the top right corner
# rather than than using the exit button.
window.protocol('WM_DELETE_WINDOW', exitProgram)

# Creating Edit submenu
editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=undo, accelerator='Ctrl+Z')
editMenu.add_command(label='Redo', command=redo, accelerator='Ctrl-Y')
editMenu.add_separator()
editMenu.add_command(label='Cut', command=cut, accelerator='Ctrl+X')
editMenu.add_command(label='Copy', command=copy, accelerator='Ctrl+C')
editMenu.add_command(label='Paste', command=paste, accelerator='Ctrl+V')
editMenu.add_command(label='Delete', command=deleteText, accelerator='Del')
editMenu.add_separator()
editMenu.add_command(label='Select All', command=selectAll,
                     accelerator='Ctrl+A')

# Creating text window & scrollbar
textBox = tkst.ScrolledText(window, wrap=WORD, undo=True)
textBox.pack(fill=BOTH, expand=1)

# Creating key bindings
window.bind('<Control-n>', newFile)
window.bind('<Control-o>', openFile)
window.bind('<Control-s>', save)
window.bind('<Control-Shift-S>', saveAs) # SIDE-NOTE: You need the captil 'S'
window.bind('<Control-x>', cut)          # here because of holding down shift
window.bind('<Control-c>', copy)
window.bind('<Control-v>', paste)
window.bind('<Delete>', deleteText)
window.bind('<Control-z>', undo)
window.bind('<Control-y>', redo)
window.bind('<Control-a>', selectAll)

# Keeps the window from closing
window.mainloop()