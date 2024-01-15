import tkinter as tk
from tkinter import ttk

def buttonFunction():
    print(stringVar.get())
    stringVar.set("button pressed")

# window
window = tk.Tk()
window.title("Tkinter variable")

# tkinter variable
stringVar = tk.StringVar(value="start value")

# widgets
label = ttk.Label(master=window, textvariable=stringVar)
label.pack()

entry = ttk.Entry(master=window, textvariable=stringVar)
entry.pack()

button = ttk.Button(master=window, text="a button", command=buttonFunction)
button.pack()

# exercise
# create another 2 new entry fields and 1 label. they should all be connected via a IntVar
# set start value of 0

intVar = tk.IntVar(value=0)
exercise_label = ttk.Label(master=window, textvariable=intVar)
exercise_label.pack()

exercise_entry = ttk.Entry(master=window, textvariable=intVar)
exercise_entry.pack()

exercise_entry2 = ttk.Entry(master=window, textvariable=intVar)
exercise_entry2.pack()

# run
window.mainloop()