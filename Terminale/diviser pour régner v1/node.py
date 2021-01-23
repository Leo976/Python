from fusion import fusion

class Node:

	def __init__(self, LIST):
		
		self.LIST = LIST # [a, b, c, d, e, f]
		self.LEFT = None # Node([a, b, c])
		self.RIGHT = None # Node([d, e, f])

	def tri(self):

		# si la liste 'self.LIST' comporte 1 élément, on ne fait rien :
		if len(self.LIST) == 1:
			return self.LIST

		# si la liste 'self.LIST' comporte 2 éléments,
		# on inverse la liste si le premier élément est supérieur au deuxième élément :
		if len(self.LIST) == 2:
			if self.LIST[0] > self.LIST[1]:
				self.LIST = self.LIST[::-1] # inverse la liste
			return self.LIST

		# on initialise la variable 'self.LEFT',
		# 'self.LEFT.LIST' correspond à la PREMIÈRE moitié de la liste 'self.LIST' :
		self.LEFT = Node(self.LIST[0 : len(self.LIST) // 2])

		# on initialise la variable 'self.RIGHT'
		# 'self.RIGHT.LIST' correspond à la DEUXIÈME moitié de la liste 'self.LIST' :
		self.RIGHT = Node(self.LIST[len(self.LIST) // 2 : len(self.LIST)])

		# fusionne la liste 'self.LEFT.LIST' et 'self.RIGHT.LIST' :
		self.LIST = fusion(self.LEFT.tri(), self.RIGHT.tri())

		return self.LIST