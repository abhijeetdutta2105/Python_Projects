# Tkinter layout managers: pack(), place() and grid()
# without using these layout managers you won't be able to get your widgets on the screen

# pack just packs each widget and displays it is vaguely logical format starting from top and going to the bottom by
# default aligning it to center

# you can change the above behavior by packing everything from left using side='left'

# place is all about precise positioning. you mention the x and y, and it puts it at that position. But it is very
# difficult to work out the coordinate system for case when you have lots of widgets

# grid : you can divide your screen into rows and columns and then work out.
# it is relative to other widgets.
# Also, you can't then use other geometry pack managers like place and pack with grid.
from tkinter import *

window = Tk()
window.title('Layout Manager')
window.minsize(height=500, width=500)

# you can add padding around your components too
# like this you can also add padding around single widget too
window.config(padx=100, pady=100)
label = Label(text='I am a Label', font=('Arial', 20, 'bold'))
label.grid(column=0, row=0)


def button_clicked():
    print('Button clicked!')
    print(entry.get())


button = Button(text='Button', command=button_clicked)
button.grid(column=1, row=1)

entry = Entry(width=10)
entry.grid(column=2, row=2)
window.mainloop()
