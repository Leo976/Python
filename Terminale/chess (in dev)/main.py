from functions import *
from pieces import *
import pygame

pygame.init()

# variables globales :

window = pygame.display.set_mode((400, 400))
images = load_images()
pieces = [Tour('black', [0, 0]), Cavalier('black', [1, 0]), Fou('black', [2, 0]), Dame('black', [3, 0]), Roi('black', [4, 0]), Fou('black', [5, 0]), Cavalier('black', [6, 0]), Tour('black', [7, 0]),
		  Pion('black', [0, 1]), Pion('black', [1, 1]), Pion('black', [2, 1]), Pion('black', [3, 1]), Pion('black', [4, 1]), Pion('black', [5, 1]), Pion('black', [6, 1]), Pion('black', [7, 1]),
		  Pion('white', [0, 6]), Pion('white', [1, 6]), Pion('white', [2, 6]), Pion('white', [3, 6]), Pion('white', [4, 6]), Pion('white', [5, 6]), Pion('white', [6, 6]), Pion('white', [7, 6]),
		  Tour('white', [0, 7]), Cavalier('white', [1, 7]), Fou('white', [2, 7]), Dame('white', [3, 7]), Roi('white', [4, 7]), Fou('white', [5, 7]), Cavalier('white', [6, 7]), Tour('white', [7, 7])]

# lancement du jeu :

if __name__ == '__main__':

	game = True
	
	while game:
		for player in ['black', 'white']:
			play(window, images, pieces, player)

input()