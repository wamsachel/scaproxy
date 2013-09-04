import curses

class UserInterface:
	def __init__(self, screen):
		(self.max_y, self.max_x) = screen.getmaxyx()
		self.parent_pad = curses.newpad(self.max_y, self.max_x)
		#Create 4 subpads
		self.topleft_pad = SubPad(parent_pad, )	

class SubPad:
	def __init__(self, parent_pad):
		self.subpad = curses.subpad(parent_pad,  
		


