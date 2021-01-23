from pygame.locals import *
from random import *
import os,pygame

#____________Fonctions basiques____________

def str_to_list(var,sep):

	x=[(var[i]==sep)*i for i in range(len(var))]
	y=[-1]

	for i in x:
		if i!=0:
			y.append(i)

	y.append(len(var))
	new_var=list()

	for i in range(3):#!
		new_var.append(int(var[y[i]+1:y[i+1]]))

	return new_var





def select_card(color):

	cards=variables['cards_player_'+color]

	length_cards=(len(cards)-1)*100+175
	start=1335+(585-length_cards)//2
	end=start+length_cards-175
	pos_list=list(range(start,end+1,100))

	while True:
		for event in pygame.event.get():
			
			for x1 in pos_list:

				if x1<pygame.mouse.get_pos()[0]<x1+(100 if pos_list.index(x1)!=len(pos_list)-1 else 175) and 400<pygame.mouse.get_pos()[1]<680:
					
					print_fond()
					print_pions()	
					print_cards(color,pos_list.index(x1))

					while x1<pygame.mouse.get_pos()[0]<x1+175 and 400<pygame.mouse.get_pos()[1]<680:
						for event in pygame.event.get():
							if event.type==MOUSEBUTTONDOWN and event.button==1:
								print_fond()
								print_pions()	

								return pos_list.index(x1)

					print_fond()
					print_pions()	
					print_cards(color,-1)



def select_pion(color,pions_exit):

	if pions_exit==1:
		return [i[0]!=None for i in variables['pions_player_'+color]].index(True)

	xy_pions=list()
	for i in variables['pions_player_'+color]:
		if i[0]!=None:
			xy_pions.append(cases[i[0]][i[1]-1])

	for i in range(len(xy_pions)):
		for color_case,pos_case in cases.items():
			if xy_pions[i] in pos_case:
				xy_pions[i].append(color_case)

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()

			print_fond()
			print_pions()
			print_cards(color,-1)
			
			refresh=True
			for i in xy_pions:
				if i[0]<pygame.mouse.get_pos()[0]<i[0]+49 and i[1]<pygame.mouse.get_pos()[1]<i[1]+49:
					window.blit(images['select_case'],(i[0]-13,i[1]-13))
					print_pions()
					refresh=False
					if event.type==MOUSEBUTTONDOWN and event.button==1:
						return variables['pions_player_'+color].index([i[3],i[2]])
				elif refresh:
					print_fond()
					print_pions()
					print_cards(color,-1)
				
			pygame.display.flip()

#____________Paramètres des cartes____________
	
def exit_pion(color):

	for i in range(4):
		if variables['pions_player_'+color][i][0]==None:
			variables['pions_player_'+color][i]=['cases_'+color,1]
			return

def move_pion(color,n_cases,pion):

	if go_home():
		return

	variables['pions_player_'+color][pion][1]+=n_cases

	if variables['pions_player_'+color][pion][1]>16:
		variables['pions_player_'+color][pion][1]-=16
		for i in [['black','blue'],['blue','green'],['green','red'],['red','black']]:
			if variables['pions_player_'+color][pion][0]=='cases_'+i[0]:
				variables['pions_player_'+color][pion][0]='cases_'+i[1]
				return

def start_or_forward_pions(color,pions_exit,card):

	if int(input('Exit/Forward ? (0/1) >> '))==0:
		exit_pion(color)
	else:
		pion=select_pion(color,pions_exit)
		move_pion(color,card,pion)

def go_home():

	print('go_home')
	return False

def not_pionnier():

	print('not_pionnier')
	return True

def joker():
	print('joker')

#____________Initialisation____________

def pioche(n_cards):

	x=list()

	for i in range(n_cards):
		r=randint(0,len(deck)-1)
		x.append(deck[r])
		del deck[r]

	return x