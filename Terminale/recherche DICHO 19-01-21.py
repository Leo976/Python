import unittest

from os import system

my_list = [0, 2, 4, 8, 16]



def find(new_list, element):

    # si la liste 'new_list' est vide :
    if len(new_list) == 0:
        return False

    # la variable 'key' est égale à la longeur de la liste divisé par 2 :
    key = len(new_list) // 2

    # si la variable 'element' est égale à l'élément qui se situe au milieu de la liste :
    if element == new_list[key]:
        return True

    # si la variable 'element' est inférieur à l'élément qui se situe au milieu de la liste :
    if element < new_list[key]:
        return find(new_list[0 : key], element)

    # si la variable 'element' est supérieur à l'élément qui se situe au milieu de la liste :
    if element > new_list[key]:
        return find(new_list[key + 1 : len(new_list)], element)



class MyClass(unittest.TestCase):

    def test(self):

        # si la liste est vide -> la fonction retourne False :
        self.assertFalse(find([], 0))

        # si la liste n'est pas vide ET que l'élément se trouve dans la liste -> la fonction retourne True :
        self.assertTrue(find([0, 2, 4], 0))

        # si la liste n'est pas vide ET que l'élément ne se trouve pas dans la liste -> la fonction retourne False :
        self.assertFalse(find([0, 2, 4], -1))



if __name__ == '__main__':

    unittest.main()
    print(find(my_list, 2048))

system("pause")