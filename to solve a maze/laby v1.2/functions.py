from os import system
import time
import variables



# additionne 2 tuples (a, b) + (c, d) = (a + c, b + d) :
def sum_two_tuples(tuple1, tuple2):

	return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

# recherche dans un nœud une position :
def search_initial_position(node, initial_position):

	if node.initial_position == initial_position:
		return True

	if len(node.nodes) == 0:
		return False

	for node2 in node.nodes:
		if search_initial_position(node2, initial_position):
			return True

	return False

# recherche dans un nœud la position finale puis renvoie le chemin [start_position, (X, Y), (X, Y), ... end_position] :
def search_end_position(node, end_position, paths = list()):

	if node.initial_position == end_position:
		paths.append(node.initial_position)
		return paths

	if end_position in node.nodes:
		for i in range(len(node.nodes)):
			if end_position == node.nodes[i]:
				paths.append(node.nodes[i])
				return paths

	if len(node.nodes) == 0:
		return paths

	for node2 in node.nodes:
		paths.append(node.initial_position)
		paths = search_end_position(node2, end_position, paths)
		if end_position in paths:
			break
		del paths[len(paths) - 1]

	return paths

# télécharge le fichier 'matrix.txt' puis le convertit en une matrix :
def matrix_load():

	file = open('matrix.txt')

	text = file.read() # text = '11111\n10100\n00001\n10101\n11111'
	text = text.split() # text = ['11111', '10100', '00001', '10101', '11111']
	text = [[int(k) for k in list(i)] for i in text] # text = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], ...]
	
	file.close()

	return text

# permet d'obtenir la valeur de la matrix qui se situe à gauche, en haut, à droite ou en bas de la position initiale :
def matrix_value(initial_position, direction):

	position = sum_two_tuples(initial_position, direction)

	if position[0] == -1:
		return 1

	if position[0] == len(variables.matrix[0]):
		return 1

	if position[1] == -1:
		return 1

	if position[1] == len(variables.matrix):
		return 1

	return variables.matrix[position[1]][position[0]]

# recherche dans le labyrinthe le début et la fin :
def init_start_end_positions():

	start, end = None, None

	for y in range(len(variables.matrix)):
		for x in range(len(variables.matrix[0])):
			if variables.matrix[y][x] == 8:
				start = (x, y)
			if variables.matrix[y][x] == 9:
				end = (x, y)

	return start, end

# lance l'animation du personnage dans le labyrinthe :
def play_animation():

	for path in variables.paths:

		for y in range(len(variables.matrix)):
			for x in range(len(variables.matrix[0])):

				if (path == (x, y)):
					print('A', end='')
				elif variables.end_position == (x, y):
					print('$', end='')
				else:
					print('■' if variables.matrix[y][x] == 1 else '□', end='')

			print()

		time.sleep(1/2)
		system('cls')