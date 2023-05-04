from tkinter import *
from tkinter.ttk import *

root = Tk()

root.geometry("700x400")

txtInput = Text(root, borderwidth=0, highlightthickness=0, wrap="word", width=40, height=4)
txtInput.pack(side=BOTTOM)

root.mainloop()
