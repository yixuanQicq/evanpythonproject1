import tkinter as tk
# contains all the widget we are going to use
import ttkbootstrap as ttk

def convert():
    miles_input = entryInt.get()
    output_text = miles_input * 1.61
    outputString.set(output_text)

# window
window = ttk.Window(themename="minty")
window.title("random demo")
window.geometry("300x150")

# title
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entryInt = tk.DoubleVar()
entry = ttk.Entry(master=input_frame, textvariable=entryInt)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# output
outputString = tk.StringVar()
output_label = ttk.Label(master=window, font="Calibri 24", textvariable=outputString)
output_label.pack(pady=5)

# run
window.mainloop()
