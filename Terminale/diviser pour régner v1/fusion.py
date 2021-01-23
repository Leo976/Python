# fusionne deux listes TRIÉES en une liste triée :
def fusion(list1, list2):

	list3 = list()

	while len(list1) * len(list2) != 0:

		if list1[0] <= list2[0]:
			list3.append(list1[0])
			del list1[0]
			
		elif list1[0] > list2[0]:
			list3.append(list2[0])
			del list2[0]
			
	if len(list1) == 0:
		return list3 + list2
	
	if len(list2) == 0:
		return list3 + list1