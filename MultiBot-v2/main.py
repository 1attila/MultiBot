from tkinter import ttk
from tkinter import *
#import MultiBot

def main(): #build GUI
    root = Tk()
    Frame = ttk.Frame(root, padding=10, height=400, width=500)
    Label = ttk.Label(root, padding=10)
    Frame.pack()
    Label.pack()
    root.mainloop()

main()