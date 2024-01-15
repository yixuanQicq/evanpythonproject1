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

# place layout
#label1.place(x = 200, y = 100, width= 100, height = 200)
label2.place(relx = 0.2, rely = 0.1, relwidth=0.4, relheight = 0.5 )

# run
window.mainloop()