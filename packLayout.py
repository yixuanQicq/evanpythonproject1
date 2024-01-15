import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Pack")
window.geometry("400x600")

# widget
label1 = tk.Label(master=window, text="First Label", background='red')
label2 = tk.Label(master=window, text="Label 2", background='green')
label3 = tk.Label(master=window, text="Last of the label", background='blue')
button = ttk.Button(master=window, text="Button")

#layout
label1.pack(side="top", fill = 'both', ipady = 200, ipadx = 100)
label2.pack(side="top", expand = True, fill = 'both')
label3.pack(side="top", expand = True, fill = 'both')
button.pack(side="top", fill = 'x')

# run
window.mainloop()