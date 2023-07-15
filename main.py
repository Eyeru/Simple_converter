# Python program to  create a simple GUI
# weight converter using Tkinter


from tkinter import *

# Create a GUI window
window = Tk()


# Function to convert weight
# given in kg to grams, pounds
# and ounces
def from_br():
    # convert kg to gram
    dollar = float(e2_value.get()) * 50

    # convert kg to pound
    pound = float(e2_value.get()) * 70

    # convert kg to ounce
    euro = float(e2_value.get()) * 80
    # Enters the converted weight to
    # the text widget
    t1.delete("1.0", END)
    t1.insert(END, dollar)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, euro)


# Create the Label widgets
e1 = Label(window, text="Enter the amount in Birr")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
b1 = Button(window, text="Submit", command=from_br, bg="grey", fg="black")


# grid method is used for placing
# the widgets at respective positions
# in table like structure
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)


b1.grid(row=0, column=2)


a3 = Label(window, text='Dollar')
a4 = Label(window, text='Pound')
a5 = Label(window, text='Euro')

# Create the Text Widgets
t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

t1.grid(row=4, column=0)
t2.grid(row=4, column=1)
t3.grid(row=4, column=2)

a3.grid(row=5, column=0)
a4.grid(row=5, column=1)
a5.grid(row=5, column=2)
# Start the GUI
window.mainloop()
