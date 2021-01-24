from functions import *
from directions import *

class Pion:

	def __init__(self, color, initial_position):
		
		self.color = color
		self.initial_position = initial_position

	def search_future_positions(self, pieces):

		future_positions = list()

		if self.color == 'black':
			future_positions.append(tp_position(self.initial_position, [DOWN]))
			if self.initial_position[1] == 1: # si c'est son premier déplacement
				future_positions.append(tp_position(self.initial_position, [DOWN, DOWN]))
	
		if self.color == 'white':
			future_positions.append(tp_position(self.initial_position, [UP]))
			if self.initial_position[1] == 6: # si c'est son premier déplacement
				future_positions.append(tp_position(self.initial_position, [UP, UP]))

		return future_positions

class Cavalier:

	def __init__(self, color, initial_position):
		
		self.color = color
		self.initial_position = initial_position

	def search_future_positions(self, pieces):

		future_positions = list()

		future_positions.append(tp_position(self.initial_position, [LEFT, LEFT, UP]))
		future_positions.append(tp_position(self.initial_position, [LEFT, UP, UP]))
		future_positions.append(tp_position(self.initial_position, [RIGHT, UP, UP]))
		future_positions.append(tp_position(self.initial_position, [RIGHT, RIGHT, UP]))
		future_positions.append(tp_position(self.initial_position, [RIGHT, RIGHT, DOWN]))
		future_positions.append(tp_position(self.initial_position, [RIGHT, DOWN, DOWN]))
		future_positions.append(tp_position(self.initial_position, [LEFT, DOWN, DOWN]))
		future_positions.append(tp_position(self.initial_position, [LEFT, LEFT, DOWN]))

		return future_positions

class Tour:

	def __init__(self, color, initial_position):
		
		self.color = color
		self.initial_position = initial_position

	def search_future_positions(self, pieces):

		future_positions = list()

		for x in range(8):
			future_positions.append([x, self.initial_position[1]])

		for y in range(8):
			future_positions.append([self.initial_position[0], y])

		future_positions.remove(self.initial_position)
		future_positions.remove(self.initial_position)

		return future_positions

class Fou:

	def __init__(self, color, initial_position):
		
		self.color = color
		self.initial_position = initial_position

	def search_future_positions(self, pieces):

		future_positions = list()

		for i in range(1, 8):
			future_positions.append(tp_position(self.initial_position, [RIGHT, UP] * i))

		for i in range(1, 8):
			future_positions.append(tp_position(self.initial_position, [LEFT, UP] * i))

		for i in range(1, 8):
			future_positions.append(tp_position(self.initial_position, [LEFT, DOWN] * i))

		for i in range(1, 8):
			future_positions.append(tp_position(self.initial_position, [RIGHT, DOWN] * i))

		return future_positions

class Dame:

	def __init__(self, color, initial_position):
		
		self.color = color
		self.initial_position = initial_position

	def search_future_positions(self, pieces):

		future_positions = list()

		cavalier = Cavalier(self.color, self.initial_position)
		future_positions += cavalier.search_future_positions()

		fou = Fou(self.color, self.initial_position)
		future_positions += fou.search_future_positions()

		roi = Roi(self.color, self.initial_position)
		future_positions += roi.search_future_positions()

		return future_positions

class Roi:

	def __init__(self, color, initial_position):
		
		self.color = color
		self.initial_position = initial_position

	def search_future_positions(self, pieces):

		future_positions = list()

		future_positions.append(tp_position(self.initial_position, [RIGHT]))
		future_positions.append(tp_position(self.initial_position, [RIGHT, UP]))
		future_positions.append(tp_position(self.initial_position, [UP]))
		future_positions.append(tp_position(self.initial_position, [UP, LEFT]))
		future_positions.append(tp_position(self.initial_position, [LEFT]))
		future_positions.append(tp_position(self.initial_position, [LEFT, DOWN]))
		future_positions.append(tp_position(self.initial_position, [DOWN]))
		future_positions.append(tp_position(self.initial_position, [DOWN, LEFT]))

		return future_positions