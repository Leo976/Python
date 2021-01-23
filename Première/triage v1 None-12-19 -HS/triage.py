import os

data={'.txt':'traitement de textes','.mp4':'vidéos'}
CD='F:/NSI 2019-2020/Python/triage v1/'

folder=os.listdir("F:/NSI 2019-2020/Python/triage v1")

for i in folder:
	for tag,file in data.items():
		if tag in i:
			os.rename(CD+i,CD+data[tag]+'/'+i)