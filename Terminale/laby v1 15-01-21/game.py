import os, time



file = open('file.txt')

text = file.read() # text = '11111\n10100\n00001\n10101\n11111'
text = text.split() # text = ['11111', '10100', '00001', '10101', '11111']

matrix = []

for y in range(len(text)):

	sub_matrix = []

	for x in range(len(text[y])):
		sub_matrix.append(int(text[y][x]))

	matrix.append(sub_matrix)

file.close()



class Player:

	def __init__(self, x, y, r):

		self.x = x
		self.y = y
		self.r = r

	def turn_left(self):

		if ((self.y == 0 and self.r == 0) or (self.x == len(matrix[0]) - 1 and self.r == 1) or (self.y == len(matrix) - 1 and self.r == 2) or (self.x == 0 and self.r == 3)):
			return False

		if self.r == 0 and matrix[self.y - 1][self.x] != 1:
			self.y -= 1
			self.r = 3
			return True

		if self.r == 1 and matrix[self.y][self.x + 1] != 1:
			self.x += 1
			self.r = 0
			return True

		if self.r == 2 and matrix[self.y + 1][self.x] != 1:
			self.y += 1
			self.r = 1
			return True

		if self.r == 3 and matrix[self.y][self.x - 1] != 1:
			self.x -= 1
			self.r = 2
			return True

		return False



def print_laby():

	matrix[player.y][player.x] = 2

	for y in matrix:
		print(y)

	matrix[player.y][player.x] = 0

def print_player():

	print('\n')
	print(['>', 'v', '<', '^'][player.r])



player = Player(1, 2, 0)

while matrix[player.y][player.x] != 9:

	print_laby()
	print_player()

	if not(player.turn_left()):
		player.r = (player.r + 1) % 4

	time.sleep(1)
	os.system('cls')



os.system('pause')






# Léo