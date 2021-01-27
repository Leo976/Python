from matrix import Matrix
from os import system



# Condition de base : matrix.read(line, column) == 0
# Vérifie si la case est égale à 0 : à droite, en haut, à gauche & en bas
# Si c'est vraie, faire la même chose avec cette nouvelle case, puis finir les autres directions :
def find_voids(line, column, positions = list()):

	for position in [(line, column + 1), (line - 1, column), (line, column - 1), (line + 1, column)]:
		if not(matrix_answer.out_of_dimension(*position)):
	
			if matrix_answer.read(*position) == 0 and not(position in positions):
				positions.append(position)
				positions = find_voids(*position, positions)
	
	return positions

# Condition de base : matrix.read(line, column) == 0
# Vérifie si la case n'est pas égale à 0 : à droite, en haut à droite, en haut, à gauche en haut, à gauche, à gauche en bas & en bas
# Si c'est vraie, dévoilé la case, puis finir les autres directions :
def find_borders(line, column, positions = list()):

	if matrix_answer.read(line, column) == 0:

		for i in range(line - 1, line + 2):
			for j in range(column - 1, column + 2):

				position = (i, j)

				if not(matrix_answer.out_of_dimension(*position)):
			
					if not(position in positions):
						matrix_player.edit(*position, matrix_answer.read(*position))
						positions.append(position)
						positions = find_borders(*position, positions)
	
	return positions

# Vérifie si la matrice ne possèdent que des bombes :
def player_win():

	for line in range(matrix_player.nb_line):
		for column in range(matrix_player.nb_column):
			if matrix_player.read(line, column) == -1 and matrix_answer.read(line, column) != 9:
				return False

	return True



matrix_answer = Matrix(10, 10)
matrix_answer.generate_bombs(5)
matrix_answer.generate_numbers()

matrix_player = Matrix(10, 10)



while True:

	system('cls')
	matrix_answer.draw()
	print()
	matrix_player.draw()
	print()

	line = int(input('Ligne = ')) - 1
	column = int(input('Colonne = ')) - 1

	if matrix_player.out_of_dimension(line, column):
		continue

	if matrix_answer.read(line, column) == 9:
		print()
		print('Tu as perdu !')
		break

	if matrix_player.read(line, column) != -1:
		continue

	if matrix_answer.read(line, column) == 0:
		for position in find_voids(line, column):
			matrix_player.edit(*position, matrix_answer.read(*position))
		find_borders(*position)
	else:
		matrix_player.edit(line, column, matrix_answer.read(line, column))

	if player_win():
		print()
		print('Tu as gagné !')
		break

input()
