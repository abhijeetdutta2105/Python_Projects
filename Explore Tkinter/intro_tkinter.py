# Tkinter module is inbuilt in Python that can be used to create GUI

import tkinter

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text='I am a label', font=("Arial", 20, "bold"))
# pack() is used to control where the component should come
# you can use keyword side and mention the value to refer to the position of the component
my_label.pack()


# you can use tkinter.config() and mention the properties you want to change using keywords

def button_clicked():
    my_label.config(text=input.get())


# button
button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry()
input.pack()
# you can use input.get() to get the text entered in the box, you can also set the width of the entry component


# mainloop() keeps on listening for the user inputs and will show the window on the screen
# this line has to be at the end of the program
window.mainloop()
