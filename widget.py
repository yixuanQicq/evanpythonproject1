import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("widget demo")
window.geometry('800x500')

# widgets
label_widget = ttk.Label(master=window, text="this is a label widget")
label_widget.pack()

text_widget = tk.Text(master=window)
text_widget.pack()

entry_widget = ttk.Entry(master=window)
entry_widget.pack()

exercise_label = ttk.Label(master=window, text="my label")
exercise_label.pack()

button_widget = ttk.Button(master=window, text="A button", command=lambda: print("hi"))
button_widget.pack()

exercise_button = ttk.Button(master=window, text="exercise button", command=lambda: print("hello"))
exercise_button.pack()

# run
window.mainloop()

# exercise
# add one more text label and a button with a function that prints 'hello'
# the label should say "my label" and be between the entry widget and the button