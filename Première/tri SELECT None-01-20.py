#Tri par séléction:

my_list=[5,4,1,8,1.4,90,234,111,4]

for i in range(len(my_list)):
	i_index=i
	for x in range(i,len(my_list)):
		if my_list[x]<my_list[i_index]:
			i_index=x

	my_list.insert(i,my_list[i_index])
	del my_list[i_index+1]

input(my_list)