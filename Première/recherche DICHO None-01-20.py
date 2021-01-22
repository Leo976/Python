#Recherche par dichotomie:

my_list,find=[4,8,11,30,52,201,251],7

while True:
	f=len(my_list)//2
	if my_list[f]==find:
		input(True);break
	if f==0:
		input(False);break
	if my_list[f]<find:
		my_list=my_list[f:len(my_list)]
	else:
		my_list=my_list[0:f]