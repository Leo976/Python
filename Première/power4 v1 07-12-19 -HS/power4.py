import pygame,time
from pygame.locals import *

pygame.init()
window=pygame.display.set_mode((240,240),pygame.DOUBLEBUF)
pygame.display.set_caption('Power4 v.1')
pygame.display.set_icon(pygame.image.load('logo.png').convert_alpha())

fond=pygame.image.load('fond.png')
P1=pygame.image.load('P1.png')
P2=pygame.image.load('P2.png')
W1=pygame.image.load('W1.png')
W2=pygame.image.load('W2.png')
W0=pygame.image.load('W0.png')

def design():
	window.blit(fond,(0,0))
	for y in range(6):
		for x in range(7):
			if cases[y][x]>0:
				window.blit(P1 if cases[y][x]==1 else P2,((2+3*x)*10,(5+3*y)*10))
def win(u):
	if u==1 or u==16:
		design()
		window.blit(W1 if u==1 else W2,(0,0))
		pygame.display.flip()
		time.sleep(2)
		return True
	return False

cases=[[0]*7 for i in range(6)]
PX=1
curseur=20

combinations=list()
for i in range(3):
	for n in range(0,61,10):
		combinations.append(n+i)
combinations=[(combinations[0:12]),(combinations[13:24])]

def diagonal(x,y,xa,ya):
	u=1
	for n in range(4):
		print(x)
		input(y)
		u=cases[y][x]*u
		y+=ya
		x+=xa
	if win(u):
		return True
	return False

while True:
	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			pygame.quit()

		for x in range(20,210,30):
			if x<=pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0]<=x+20:
				curseur=x

		if event.type==MOUSEBUTTONDOWN and event.button==1:
			boucle=True
			for y in range(5,-1,-1):
				x=[i==curseur for i in range(20,210,30)].index(True)
				if cases[y][x]==0 and boucle:
					boucle=False
					cases[y][x]=PX
					PX=1 if PX==2 else 2

	#horizontal_win
	for y in range(6):
		for x in range(4):
			u=1
			for i in range(4):
				u=cases[y][x+i]*u
			if win(u):
				cases=[[0]*7 for i in range(7)]

	#vertical_win
	for x in range(7):
		for y in range(3):
			u=1
			for i in range(4):
				u=cases[y+i][x]*u
			if win(u):
				cases=[[0]*7 for i in range(7)]

	#diagonal_win
	for i in combinations[0]:
		n=list(str(i))
		if len(n)==1:
			n.append('0')
		if diagonal(int(n[0]),int(n[1]),-1,1):
			cases=[[0]*7 for i in range(7)]
	for i in combinations[1]:
		n=list(str(i))
		if len(n)==1:
			n.append('0')
		if diagonal(int(n[0]),int(n[1]),1,1):
			cases=[[0]*7 for i in range(7)]

	#equality
	u=1
	for y in range(6):
		for x in range(7):
			u=cases[y][x]*u
	if u>0:
		window.blit(W0,(0,0))
		pygame.display.flip()
		time.sleep(2)
		cases=[[0]*7 for i in range(7)]

	design()
	window.blit(P1 if PX==1 else P2,(curseur,20))
	pygame.display.flip()