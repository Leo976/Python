from pygame.locals import *
from random import *
import pygame,time

pygame.init()
window=pygame.display.set_mode((1920,1080))
fond=pygame.image.load('images/fond.png')
window.blit(fond,(0,0))

for file in ['letter_'+'abcdefghijklmnopqrstuvwxyz'[i] for i in range(26)]:
	vars()[file]=pygame.image.load('images/letters/{}.png'.format(str(file)))
	print(vars()[file],'>>',file)
for file in ['life_{}'.format(i) for i in range(7)]:
	vars()[file]=pygame.image.load('images/lifes/{}.png'.format(str(file)))
	print(vars()[file],'>>',file)
for file in ['hit_life_{}'.format(i) for i in range(7)]:
	vars()[file]=pygame.image.load('images/hit_lifes/{}.png'.format(str(file)))
	print(vars()[file],'>>',file)
for file in ['win','lost','space']:
	vars()[file]=pygame.image.load('images/{}.png'.format(str(file)))
	print(vars()[file],'>>',file)

def key(x):
	if 123>x and x>96:
		x='abcdefghijklmnopqrstuvwxyz'[x-97]
		if x=='q':
			return 'a'
		if x=='a':
			return 'q'
		if x=='z':
			return 'w'
		if x=='w':
			return 'z'
		return x
	elif x==59:
		return 'm'
	elif x==8:
		return False
	elif x==13:
		return True
	else:
		return -1

file=list(open('words.txt','r'))
for i in range(len(file)-1):
	print(file[i][0:len(file[i])-1])
	file[i]=file[i][0:len(file[i])-1]
word_answear=list(file[randint(0,len(file)-1)])
word_player=['-']*len(word_answear)
letters=list()
life=6

while True:
	
	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			pygame.quit()

		if event.type==KEYDOWN:
			letter=key(event.key)

			if type(letter)==str and letter in word_answear and not(letter in word_player):
				letters.append(letter)
				for ix in range(len(word_answear)):
					if word_answear[ix]==letter:
						word_player[ix]=letter

			elif type(letter)==str and not(letter in letters):
				letters.append(letter)
				for ix in ['hit_life_{}'.format(life),'life_{}'.format(life)]*4:
					window.blit(vars()[ix],(80,120))
					pygame.display.flip()
					time.sleep(1/8)
				life-=1

			else:
				print('#!?')

			if not('-' in word_player) or life==0:				
				word_player=word_answear

	window.blit(fond,(0,0))
	x,y=400,140
	x_space=80
	for letter in word_player:
		if letter=='-':
			window.blit(space,(x,y))
		else:
			window.blit(vars()['letter_{}'.format(letter)],(x,y))
		x+=x_space+40 if letter=='m' or letter=='w' else x_space
	window.blit(vars()['life_{}'.format(life)],(80,120))
	pygame.display.flip()

	if word_player==word_answear:
		window.blit(lost if life==0 else win,(760,340))
		pygame.display.flip()
		time.sleep(4)
		word_answear=list(file[randint(0,len(file)-1)])
		life=6
		word_player=['-']*len(word_answear)
		letters=list()