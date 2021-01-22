from functions import *
from node import Node
from os import system
import variables

variables.matrix = matrix_load()
variables.start_position, variables.end_position = init_start_end_positions()

variables.node = Node(variables.start_position)
variables.node.init_nodes()
variables.paths = search_end_position(variables.node, variables.end_position)
#variables.node.draw()
play_animation()

system("pause")