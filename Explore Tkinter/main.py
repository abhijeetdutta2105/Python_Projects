from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=200, pady=50)

# input entry for miles
input = Entry(width=10)
input.grid(column=1, row=0)

# label for Miles
miles_label = Label(text='Miles', font=('Arial', 14))
miles_label.config(padx=10)
miles_label.grid(column=2, row=0)

# label for Equals
equals_label = Label(text='equals', font=('Arial', 14))
equals_label.config(padx=10)
equals_label.grid(column=0, row=1)

# label for answer
answer_label = Label(text='', font=('Arial', 14))
answer_label.config(padx=10)
answer_label.grid(column=1, row=1)

# label for Km
km_label = Label(text='Km', font=('Arial', 14))
km_label.config(padx=10)
km_label.grid(column=2, row=1)


# calculate button
def convert_mile_to_km():
    mile_value = float(input.get())
    km_value = mile_value * 1.609
    km_value = int(km_value)
    answer_label.config(text=km_value)


calcuate_button = Button(text='Calcuate', font=('Arial', 12, 'bold'), command=convert_mile_to_km)
calcuate_button.grid(column=1, row=2)
window.mainloop()
