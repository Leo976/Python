from player import Player

from position import Position

import global_vars, matrix, os, time



# initialisation :

global_vars.matrix = matrix.download()

global_vars.player = Player(Position(0, 2))



# exécution :

while global_vars.matrix[global_vars.player.position.y][global_vars.player.position.x] != 9:

	matrix.draw()

	if not(global_vars.player.can_turn_left()):
		global_vars.player.rotate()
	else:
		global_vars.player.turn_left()

	time.sleep(1/2)
	os.system('cls')



# fin :

os.system('pause')