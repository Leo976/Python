def import_list():

	file = open('list.txt')

	text = file.read()
	text = text.split()
	text = [int(i) for i in text]

	return text