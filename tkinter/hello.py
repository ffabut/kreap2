import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

messagebox.showerror("Errdddor", "Error message")
messagebox.showwarning("Wardddning","Warning message")
messagebox.showinfo("Informdddation","Informative message")

window.mainloop()