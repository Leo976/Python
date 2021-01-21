from position import Position

import global_vars



def download():

	file = open('matrix.txt')

	text = file.read() # text = '11111\n10100\n00001\n10101\n11111'
	text = text.split() # text = ['11111', '10100', '00001', '10101', '11111']
	text = [[int(k) for k in list(i)] for i in text] # text = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], ...]
	
	file.close()
	
	return text

def draw():

	global_vars.matrix[global_vars.player.position.y][global_vars.player.position.x] = ['<', '^', '>', 'v'][global_vars.player.direction.value]

	for y in global_vars.matrix:
		for x in y:
			print(x, end='')
		print() # ne s'affiche pas si je ne met pas cette instruction ...

	global_vars.matrix[global_vars.player.position.y][global_vars.player.position.x] = 0