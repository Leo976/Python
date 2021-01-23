from import_list import import_list
from node import Node
from os import system

my_list = import_list()
node = Node(my_list)
my_list = node.tri()
print(my_list)

system('pause')