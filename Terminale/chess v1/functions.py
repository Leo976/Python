from os import *
import pygame
from pygame.locals import *

def load_images():

	images = dict()

	cd = path.dirname(path.realpath(__file__)) + '\\img'
	files = listdir(cd)

	for file in files:
		images[file] = pygame.image.load('img/' + file) # !

	return images

def sum_two_lists(list1, list2):

	return [list1[0] + list2[0], list1[1] + list2[1]]

def out_of_matrix(position):

	if position[0] < 0:
		return True
	
	if position[0] > 7:
		return True
	
	if position[1] < 0:
		return True
	
	if position[1] > 7:
		return True

	return False

def tp_position(initial_position, directions):

	new_initial_position = initial_position

	for direction in directions:
		new_initial_position = sum_two_lists(new_initial_position, direction)

	if out_of_matrix(new_initial_position):
		return None
	else:
		return new_initial_position

def draw_game(window, images, pieces, selected_case = list()):

	window.blit(images['background.png'], (0, 0))

	for piece in pieces:

		if selected_case == piece.initial_position:
			images[type(piece).__name__.lower() + '_' + piece.color + '.png'].set_alpha(255 / 2)
			window.blit(images[type(piece).__name__.lower() + '_' + piece.color + '.png'], (50 * piece.initial_position[0], 50 * piece.initial_position[1]))
			images[type(piece).__name__.lower() + '_' + piece.color + '.png'].set_alpha(255)
		else:
			window.blit(images[type(piece).__name__.lower() + '_' + piece.color + '.png'], (50 * piece.initial_position[0], 50 * piece.initial_position[1]))

	pygame.display.flip()

def select_case(window, images, pieces, selected_case = list()):

	while True:

		draw_game(window, images, pieces, selected_case)

		for y in range(8):
			for x in range(8):

				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
						return [event.pos[0] // 50, event.pos[1] // 50]

def play(window, images, pieces, player):

	while True:
	
		case = select_case(window, images, pieces)
	
		for piece in pieces:
			if case == piece.initial_position:
				if piece.color == player:

					new_case = select_case(window, images, pieces, case)
		
					if new_case in piece.search_future_positions(pieces):
						piece.initial_position = new_case
						return

