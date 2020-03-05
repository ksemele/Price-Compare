from tkinter import *


class Window:
	def __init__(self, width, height, title="PriceCompare TEST build", resizable=(False, False), icon=None):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry(f"{width}x{height}+800+300")  # f"" place formatted string with parsing {variables}
		self.root.resizable(resizable[0], resizable[1])  # access to resize window by X, Y
		if icon:
			self.root.iconbitmap(icon)

	def run(self):
		self.root.mainloop()
