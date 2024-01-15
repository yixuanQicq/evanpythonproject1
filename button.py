import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Buttons")
window.geometry('600x400')

def buttonFunction():
    print("I clicked on button")
    print("radio var selected: " + radioVar.get())

def radioButtonFunction():
    print("check button value: " + str(checkVar.get()))
    checkVar.set(False)

# widget
#button = ttk.Button(master=window, text="A button", command=buttonFunction)
#button.pack()

# checkbutton
checkVar = tk.BooleanVar()
checkButton = ttk.Checkbutton(
    master=window,
    text="checkbox 1",
    command=lambda: print(radioVar.get()),
    variable=checkVar)
checkButton.pack()

# radio button
radioVar = tk.StringVar()
radio1 = ttk.Radiobutton(master=window,
                         text="A",
                         value="A",
                         variable=radioVar,
                         command=radioButtonFunction)
radio1.pack()
radio2 = ttk.Radiobutton(master=window,
                         text="B",
                         value="B",
                         variable=radioVar,
                         command=radioButtonFunction)
radio2.pack()

# exercise
# create another checkbutton and 2 radio buttons
# radio button:
    # value for the buttons are A and B
    # ticking either prints the value of the checkbutton
    # ticking the radio button unchecks the checkbutton
# check button:
    # ticking the chekbutton prints the value of the radio buton value
    # use tkinter var for Booleans.



# run
window.mainloop()