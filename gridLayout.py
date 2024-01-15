import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Grid")
window.geometry("600x400")

# widgets
label1 = tk.Label(master=window, text="Label 1", background='red')
label2 = tk.Label(master=window, text="Label 2", background='green')
label3 = tk.Label(master=window, text="Label 3", background='blue')
label4 = tk.Label(master=window, text="Label 4", background='yellow')
button1 = ttk.Button(master=window, text="Button 1")
button2 = ttk.Button(master=window, text="Button 2")
entry = ttk.Entry(master=window)

# grid layout

# define a grid
window.columnconfigure(0, weight=1) # self/total , 1/6
window.columnconfigure(1, weight=1) # 1/6
window.columnconfigure(2, weight=1) # 1/6
window.columnconfigure(3, weight=3) # 3/6
window.rowconfigure(0, weight=1)

# place widget
label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=0, column=1, sticky="w")
button1.grid(row=0, column=1, sticky="s")
label3.grid(row=0, column=2, sticky="ew")
label4.grid(row=0, column=3, sticky="nsew")


# run
window.mainloop()