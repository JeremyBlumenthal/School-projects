from tkinter import *
import tkinter.messagebox
import os
from set import *

class Main:

    def __init__(self, root):
    	self.frame = Frame(root)
    	self.frame.pack()
    	self.bottom_frame = Frame(root)
    	self.bottom_frame.pack()

    	self.title_s = Label(self.frame, text = "S", font = "Helvetica 50 bold italic", foreground = "red")
    	self.title_s.pack(side = LEFT, pady = 25)
    	self.title_e = Label(self.frame, text = "E", font = "Helvetica 40 bold italic", foreground = "green")
    	self.title_e.pack(side = LEFT, pady = 25)
    	self.title_t = Label(self.frame, text = "T", font = "Helvetica 50 bold italic", foreground = "blue")
    	self.title_t.pack(side = LEFT, pady = 25)

    	self.gui_button = Button(self.bottom_frame, text = "Play - GUI", width = 15, command = self.message)
    	self.gui_button.pack(pady = 10)
    	self.terminal_button = Button(self.bottom_frame, text = "Play - Terminal", width = 15, command = self.terminal)
    	self.terminal_button.pack(pady = 5)
    	self.rules = Button(self.bottom_frame, text = "Instructions", width = 15, command = self.instructions)
    	self.rules.pack(pady = 5)

    def message(self):
    	tkinter.messagebox.showinfo("Set - GUI", "Work in progress")

    def terminal(self):
    	root.destroy()
    	play_terminal = Set()

    def instructions(self):
    	os.system("set_instructions.pdf")


if __name__ == "__main__":
    root = Tk()
    root.title("SET")
    root.geometry("300x300")
    main = Main(root)
    mainloop()
