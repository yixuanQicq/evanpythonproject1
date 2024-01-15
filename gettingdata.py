import tkinter as tk
from tkinter import ttk

def buttonFunction():
    # getting data
    # entry widget have get method
    newText = entry.get()

    # label widget don't have get method
    # print(label.get()) can't do this!!!!

    # update Label
    #label.config(text="new text")
    label["text"] = newText

    # other than updating text, we can update other attributes of widget
    entry["state"] = "disable"

    # this statement gives you all attribute you can edit
    # print(label.configure())
    # print(entry.configure())

def resetFunction():
    label["text"] = "some text"
    entry["state"] = "enabled"

# window
window = tk.Tk()
window.title("Getting and Setting widgets")

# widgets
label = ttk.Label(master=window, text="some text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="the button", command=buttonFunction)
button.pack()

exerciseButton = ttk.Button(master=window, text="Reset", command=resetFunction)
exerciseButton.pack()

# run
window.mainloop()

# exercise
# add another button called "Reset" to change the label text back to some text and enables entry