import tkinter as tk
from tkinter import ttk

window = tk.Tk()
bgimg = tk.PhotoImage(file="./photo.png")
label = tk.Label(master=window, image=bgimg)
label.pack()
window.mainloop()