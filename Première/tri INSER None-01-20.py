#Tri par insertion:

my_list=[5,4,1,8,1.4,90,234,111,4]

for i in range(1,len(my_list)):
	for x in range(i,0,-1):
		if my_list[x-1]>my_list[x]:
			my_list[x-1:x+1]=[my_list[x],my_list[x-1]]
		else:
			break
			
input(my_list)