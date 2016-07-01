# Program that allows the user to click inside the window and change their
# current cursor while inside the window.

from tkinter import * # Module used for creating GUI

# Used for switching between the different cursor types
def changeMouse(event):
	global startingMouse
	startingMouse += 1

	if startingMouse >= len(mouse):
		startingMouse = 0

	frame['cursor'] = mouse[startingMouse]

# Different cursors that are available
mouse = [
    "arrow",
    "circle",
	"clock",
    "cross",
    "dotbox",
    "exchange",
    "fleur",
    "heart",
    "man",
    "mouse",
    "pirate",
    "plus",
    "shuttle",
    "sizing",
    "spider",
    "spraycan",
    "star",
    "target",
    "tcross",
    "trek",
]

# Creates the window
window = Tk()

# Variable used for keeping track of current cursor
startingMouse = 0

# Creates a frame
frame = Frame(
	width=450, 
	height=500, 
	bd=8,
	cursor=mouse[startingMouse]
)

# Binds the left mouse button click
frame.bind('<Button-1>', changeMouse)
frame.pack()

# Keeps the window from closing
window.mainloop()