import tkinter as tk

root = tk.Tk()
root.geometry("500x200")
root.title("Snowflake")
root.configure(background="white")

a = tk.Label(root, text="Hello, World!", font=('Arial', 18))
a.config(background="black")
a.pack

root.mainloop()
