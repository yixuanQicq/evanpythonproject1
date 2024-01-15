import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("10000x10000")
window.title("Event Binding")

# window attributes
window.minsize(100, 100)
window.maxsize(800, 700)
window.resizable(True, False)
window.attributes('-alpha', 1)

# Screen Attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# widgets
text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="A button")
button.pack()


# events
#window.bind('<KeyPress>', lambda event: print("a button was pressed " + event.char))

def getPostion(event):
    print("x: " + str(event.x) + ", y: " + str(event.y))

#window.bind('<Motion>', getPostion)
window.bind('<Escape>', lambda event: window.geometry("100x100"))

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# exercise:
# print 'Mousewheel" when user holds down shift and uses the mousewheel with text(text widget) is selected.

# run
window.mainloop()