import os,itertools

def replace_letter(var,letter,new_letter):
	var=list(var)
	for i in range(len(var)):
		if var[i]==letter:
			var[i]=new_letter
	return ''.join(var)
def string_to_list(var,cut):
	L1=list()
	start=0
	end=0
	for i in range(len(var)):
		if var[i]==cut:
			L1.append(var[start:end])		
			start=i+1
			end=i+1
		else:
			end+=1
	L1.append(var[start:end])
	return L1

#convert ['txt=fichier>fichier2\n','\n',..] in ['txt=fichier1>fichier2',..]
files=list()
data=list(open('data.txt','r'))
for i in range(len(data)):
	if data[i]!='\n':
		files.append(data[i][0:len(data[i])])
files=[i[0:-1 if '\n' in i else len(i)] for i in files]

#convert ['txt=fichier1>fichier2',..] in {'.txt':'fichier1/fichier2',..}
data=dict()
for i in files:
	cut=i.find('=')
	types=i[0:cut]
	if types.find(',')!=-1:
		types=string_to_list(types,',')
		types=['.'+i for i in types]
	else:
		types=['.{}'.format(types)]
	folders=i[cut+1:len(i)]
	folders=replace_letter(folders,'>','/')
	if ',' in folders:
		x=folders.find(',')
		while folders[x]!='/':
			x-=1
		folders=(folders[0:x+1],string_to_list(folders[x+1:len(folders)],','))
	else:
		folders=[folders]
	data[tuple(types)]=folders

#search folders emplacement > C:/Admin/..
CD=list(os.path.dirname(os.path.realpath(__file__)))
CD=replace_letter(CD,'\\','/')
all_files=os.listdir(CD)

for i in all_files:
	if i!='data.txt' and i!='triage.py':
		for types,folders in data.items():

			if len(folders)==2:
				for sub_types,sub_folders in zip(types,folders[1]):
					if sub_types in i:
						os.rename(CD+'/'+i,CD+'/'+folders[0]+sub_folders+'/'+i)
			else:
				for files in types:
					if files in i:
						os.rename(CD+'/'+i,CD+'/'+folders[0]+'/'+i)