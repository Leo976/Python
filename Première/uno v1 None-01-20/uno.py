#py -3.X -m pip install pygame

from pygame.locals import *
from random import *
import os,pygame,time

images=dict()
pygame.init()
window=pygame.display.set_mode((750,500))

#__________TÉLÉCHARGMENTS DES IMAGES__________

for i in os.listdir(os.path.dirname(os.path.realpath(__file__))+'/images'):
	images[i[:-4]]=pygame.image.load('images/'+i)
	if not(i[:-4] in ('img_fond')):
		images[i[:-4]]=pygame.transform.scale(images[i[:-4]],(int(250/3),125))

#__________FONCTION DE BASE__________

def reset_cards():

	x=list()
	for color in ['green','yellow','blue','red']:
		for card in list(range(10))+['skip','inverse','+2']:#2*0!
			x.append([color,str(card)])
	return (x+[['colors','colors'],['colors','+4']])*2

def pioche(n_cards):

	x=list()
	for i in range(n_cards):
		r=randint(0,len(cards)-1)
		x.append(cards[r])
		del cards[r]
	return x

def if_click_cards(n_card):

	global tapis

	if -1<n_card<len(player_1) and event.type==MOUSEBUTTONDOWN and event.button==1:
		if player_1[n_card][0]==tapis[0] or player_1[n_card]==['colors','colors'] or player_1[n_card]==['colors','+4'] or player_1[n_card][1]==tapis[1] or tapis==['colors','+4'] or tapis==['colors','colors']:
			tapis=player_1[n_card]
			del player_1[n_card]
			return True

	return False

def if_click_pioche():

	global player_1

	if 421.75<pygame.mouse.get_pos()[0]<6061/12 and 187.5<pygame.mouse.get_pos()[1]<312.5 and event.type==MOUSEBUTTONDOWN and event.button==1:
		player_1+=pioche(1)
		return True

	return False

def check_tapis(player):

	global player_1,player_2,tapis

	if tapis[1]=='skip' or tapis[1]=='inverse':
		return not(player==1)

	if tapis[1]=='+2':
		if player==1:
			player_2+=pioche(2)
		if player==2:
			player_1+=pioche(2)
		return player==1

	if tapis==['colors','colors']:
		if player==2:
			r=randint(0,len(player_2)-1)
			tapis=player_2[r]
			del player_2[r]
		return not(player==1)

	if tapis==['colors','+4']:
		if player==1:
			player_2+=pioche(4)
		if player==2:
			player_1+=pioche(4)
			r=randint(0,len(player_2)-1)
			tapis=player_2[r]
			del player_2[r]
		return not(player==1)

	return player==1

def player_2_play():

	global player_2,tapis,pos_cards,x_mouse

	pos_cards=list_pos_cards(750)
	x_mouse=check_pos_mouse()

	print_fond()
	print_cards_player_1(750)
	print_cards_player_2(True)
	pygame.display.flip()

	time.sleep(4/3)

	for i in range(len(player_2)):
		if player_2[i][0]==tapis[0] or player_2[i][0]=='colors' or player_2[i][1]=='+4' or player_2[i][1]==tapis[1]:
			tapis=player_2[i]
			del player_2[i]
			check_win_and_pioche()
			return check_tapis(2)
	player_2+=pioche(1)

	return False

def check_win_and_pioche():

	global cards

	if len(player_1)==0:
		print('J1 win')
		os.system('pause')

	if len(player_2)==0:
		print('J2 win')
		os.system('pause')

	if len(cards)<=4:
		cards=reset_cards()

#__________AFFICHAGE DES CARTES__________

def list_pos_cards(x_mouse):

	n=len(player_1)
	step=375/n
	center_1=875/6+step/2
	center_2=(125/3)*(x_mouse!=750)
	pos_cards=[center_1+i*step-center_2 for i in range(n)]
	pos_cards.append(pos_cards[len(pos_cards)-1]+250/3)

	return [pos_cards[i]+(i-1>=x_mouse)*(250/3+center_2-step) for i in range(n+1)]

def check_pos_mouse():

	data=dict()
	for i in range(len(pos_cards)-1):
		data[pos_cards[i]]=pos_cards[i+1]
	if x_mouse==len(player_1)-1:
		data[pos_cards[-2]]=pos_cards[-2]+125

	for x1,x2 in data.items():
		if x1<pygame.mouse.get_pos()[0]<x2 and pygame.mouse.get_pos()[1]>=375:
			return pos_cards.index(x1)

	return 750

def print_fond():

	window.blit(images['img_fond'],(0,0))
	window.blit(images['img_'+tapis[0]],(234.375,187.5))
	window.blit(images['img_'+tapis[1]],(234.375,187.5))
	window.blit(images['img_hide'],(421.75,187.5))

def print_cards_player_1(n_cards_zoom):

	for x,i in zip(pos_cards,range(len(player_1))):

		card_color=images['img_'+player_1[i][0]]
		card_number=images['img_'+player_1[i][1]]

		if n_cards_zoom==i:
			y=312.5
			card_color=pygame.transform.scale(card_color,(125,int(187.5)))
			card_number=pygame.transform.scale(card_number,(125,int(187.5)))
		else:
			y=375

		window.blit(card_color,(x,y))
		window.blit(card_number,(x,y))

def print_cards_player_2(hide):

	center=(750-(375-375/len(player_2)+250/3))/2#à simplifier..
	pos_cards_2=[center+i*375/len(player_2) for i in range(len(player_2))]

	for i in range(len(player_2)):

		if hide:
			window.blit(images['img_hide'],(pos_cards_2[i],0))
		else:
			window.blit(images['img_'+player_2[i][0]],(pos_cards_2[i],0))
			window.blit(images['img_'+player_2[i][1]],(pos_cards_2[i],0))

#__________INITIALISATION__________

cards=reset_cards()
tapis=pioche(1)[0]
player_1,player_2=pioche(7),pioche(7)
x_mouse=750
winner=False

#__________ÉXÉCUTION__________

while not(winner):

	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			pygame.quit()

		for i in range(2):
			pos_cards=list_pos_cards(x_mouse)
			x_mouse=check_pos_mouse()
		
		print_fond()
		print_cards_player_1(x_mouse)
		print_cards_player_2(True)

		pygame.display.flip()

		if if_click_cards(x_mouse):
			check_win_and_pioche()
			if check_tapis(1):
				while player_2_play():
					None

		if if_click_pioche():
			while player_2_play():
				None