from os import system
from random import randint



answer = [[0 for k in range(10)] for i in range(10)]
player = [['/' for k in range(10)] for i in range(10)]



def generate_bombs(matrix, nb_bombs):

	while sum([sum(y) for y in matrix]) != 9 * nb_bombs:
		matrix[randint(0, len(matrix) - 1)][randint(0, len(matrix) - 1)] = 9

	return matrix

def generate_numbers(matrix):

	for y in range(len(matrix)):
		for x in range(len(matrix[0])):

			if matrix[y][x] == 0:

				nb_bombs = 0

				for i in range(y - 1, y + 2):
					for j in range(x - 1, x + 2):

						if not(out_of_matrix(matrix, j, i)):
							nb_bombs += matrix[i][j] == 9

				matrix[y][x] = nb_bombs

	return matrix

def out_of_matrix(matrix, x, y):

	return x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix)

def print_matrix(matrix):

	for y in matrix:
		print(y)

def virus(x, y, positions = list()):

	for position in [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]:
		if not(out_of_matrix(answer, *position)):

			if answer[position[1]][position[0]] == 0 and not(position in positions):
				positions.append(position)
				positions = virus(*position, positions)

	return positions

def matrix_full():

	void_case = len(answer) * len(answer[0])

	for y in range(len(answer)):
		for x in range(len(answer[0])):
			void_case -= answer[y][x] != 0

	return void_case == 0



answer = generate_bombs(answer, 10)
answer = generate_numbers(answer)



while True:

	system('cls')
	#print_matrix(answer)
	print_matrix(player)
	print()

	x = int(input('X = '))
	y = int(input('Y = '))

	if out_of_matrix(player, x, y):
		continue

	if answer[y][x] == 9:
		print()
		print('Tu as perdu !')
		break

	if answer[y][x] != 0:
		player[y][x] = str(answer[y][x])

	if answer[y][x] == 0:
		for position in virus(x, y):
			player[position[1]][position[0]] = str(0)

	if matrix_full():
		print()
		print('Tu as gagné !')
		break

input()