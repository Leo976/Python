from random import randint



class Matrix:

	def __init__(self, nb_line, nb_column):

		self.nb_line = nb_line
		self.nb_column = nb_column
		self.matrix = [[-1 for k in range(nb_column)] for i in range(nb_line)]

	def draw(self):

		for line in range(self.nb_line):
			for column in range(self.nb_column):
				print(self.matrix[line][column] if self.matrix[line][column] != -1 else '/', end='')
			print()

	def read(self, line, column):

		return self.matrix[line][column]

	def edit(self, line, column, value):

		self.matrix[line][column] = value

	# Compte le nombre de bombes dans la matrice :
	def count_nb_bombs(self):

		nb_bombs = 0

		for line in range(self.nb_line):
			for column in range(self.nb_column):
				nb_bombs += self.matrix[line][column] == 9

		return nb_bombs

	# Génère des bombes dans des positions aléatoires dans la matrice :
	def generate_bombs(self, nb_bombs):

		while self.count_nb_bombs() != nb_bombs:
			self.matrix[randint(0, self.nb_line - 1)][randint(0, self.nb_column - 1)] = 9

	# Vérifie si les coordonées ne dépasse pas la dimension de la matrice :
	def out_of_dimension(self, line, column):

		return line <= -1 or column <= -1 or line >= self.nb_line or column >= self.nb_column

	# Génère sur chaque case da la matrix le nb de bombe qui se situe autour de la case :
	def generate_numbers(self):

		for line in range(self.nb_line):
			for column in range(self.nb_column):
	
				if self.matrix[line][column] == -1:
	
					nb_bombs = 0
	
					for i in range(line - 1, line + 2):
						for j in range(column - 1, column + 2):
	
							if not(self.out_of_dimension(j, i)):

								nb_bombs += self.matrix[i][j] == 9
	
					self.matrix[line][column] = nb_bombs
	
		return self.matrix