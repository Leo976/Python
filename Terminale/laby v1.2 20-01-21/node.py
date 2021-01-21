from direction import Direction
from functions import *



class Node:

	def __init__(self, initial_position):

		# self.initial_position = (X, Y)
		self.initial_position = initial_position

		# self.nodes = [Node((X, Y)), Node((X, Y)), ...]
		self.nodes = list()

	# fonction qui initialise la liste 'self.nodes' :
	def init_nodes(self):

		# si la liste n'est pas vide :
		if len(self.nodes) != 0:
			return

		# ajoute la position à gauche, en haut, à droite & en bas de la position initiale (s'il peut) à la liste 'self.nodes' :
		for direction in Direction:
			
			# s'il n'y a pas de mur à/en 'direction' de la position initiale :
			if matrix_value(self.initial_position, direction.value) != 1:

				# additionne la position initiale et la direction :
				new_initial_position = sum_two_tuples(self.initial_position, direction.value)
				
				# si la nouvelle position initiale n'existe pas dans le nœuds principal :
				if not(search_initial_position(variables.node, new_initial_position)):
					self.nodes.append(Node(new_initial_position))
	
		# fait les mêmes instructions avec chaque nœuds de la liste 'self.nodes' :
		for i in range(len(self.nodes)):
			self.nodes[i].init_nodes()

	# fonction qui affiche les nœuds :
	def draw(self, level = 0):

		print('  ' * level + str(self.initial_position))

		if len(self.nodes) == 0:
			return

		for node in self.nodes:
			node.draw(level + 1)