from enum import Enum

from position import Position

import global_vars



class Direction(Enum):

	LEFT = 0
	UP = 1
	RIGHT = 2
	DOWN = 3

class Player:

	def __init__(self, position, direction = Direction(0)):

		self.position = position
		self.direction = direction

	def can_turn_left(self):

		# si le joueur se situe à la limite de la matrix, retourner False :

			# 111>1
			# 10001
			# 00100

		if self.position.y == 0 and self.direction.name == 'RIGHT':
			return False

			# 11101
			# 10001
			# ^0100

		if self.position.x == 0 and self.direction.name == 'UP':
			return False

			# 11101
			# 10001
			# 0<100
	
		if self.position.y == len(global_vars.matrix) and self.direction.name == 'LEFT':
			return False

			# 11101
			# 10001
			# 0010v

		if self.position.x == len(global_vars.matrix[0]) and self.direction.name == 'DOWN':
			return False

		# si le joueur se trouve à gauche d'un mur, retourner False :

		if self.direction.name == 'LEFT' and global_vars.matrix[self.position.y + 1][self.position.x] == 1:
			return False

		if self.direction.name == 'UP' and global_vars.matrix[self.position.y][self.position.x - 1] == 1:
			return False

		if self.direction.name == 'RIGHT' and global_vars.matrix[self.position.y - 1][self.position.x] == 1:
			return False

		if self.direction.name == 'DOWN' and global_vars.matrix[self.position.y][self.position.x + 1] == 1:
			return False

		# le joueur peut tourner à gauche :

		return True

	def turn_left(self):

		if self.direction.name == 'LEFT':

			# 11101              11101  
			# 1<001      ->		 10001
			# 00100              0v100

			self.position.y += 1
			self.direction = Direction.DOWN

		elif self.direction.name == 'UP':

			# 11101              11101  
			# 100^1      ->		 10<01
			# 00100              00100

			self.position.x -= 1
			self.direction = Direction.LEFT

		elif self.direction.name == 'RIGHT':

			# 11101              111^1  
			# 100>1      ->		 10001
			# 00100              00100

			self.position.y -= 1
			self.direction = Direction.UP

		elif self.direction.name == 'DOWN':

			# 11101              11101  
			# 1v001      ->		 10>01
			# 00100              00100

			self.position.x += 1
			self.direction = Direction.RIGHT

	def rotate(self):

		# fait une rotation de -90° :

		if self.direction.name == 'LEFT':
			self.direction = Direction.UP

		elif self.direction.name == 'UP':
			self.direction = Direction.RIGHT

		elif self.direction.name == 'RIGHT':
			self.direction = Direction.DOWN

		elif self.direction.name == 'DOWN':
			self.direction = Direction.LEFT