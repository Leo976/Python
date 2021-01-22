import pygame,time
from pygame.locals import *

pygame.init()
window=pygame.display.set_mode((480,480))
pygame.display.set_caption('Morpion v.3')
pygame.display.set_icon(pygame.image.load('logo.png').convert_alpha())

cases=pygame.image.load('cases.png')
P1=pygame.image.load('P1.png')
P2=pygame.image.load('P2.png')
W1=pygame.image.load('W1.png')
W2=pygame.image.load('W2.png')
W0=pygame.image.load('W0.png')

def click(x1,x2,y1,y2):
	return event.pos[0]>=x1*15 and event.pos[0]<=x2*15 and event.pos[1]>=y1*15 and event.pos[1]<=y2*15

combination=((7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1))
reset=True

while True:

	#data==[key,(x,y),J] >> [[1,(2,20),0],[2,(11,20),0],[3,(20,20),0]...[9,(20,2),0]]
	if reset:
		time.sleep(2)
		window.blit(cases,(0,0))
		data=list()
		J,key=1,1
		for y in range(21,4,-8):
			for x in range(5,22,8):
				data.append([key,(x,y),0])
				key+=1
		reset=False

	produit=1
	for i in range(9):
		produit=produit*data[i][2]
	if produit!=0:
		window.blit(W0,(0,0))
		reset=True

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
		if event.type==MOUSEBUTTONDOWN and event.button==1:
			for y in range(5,22,8):
				for x in range(5,22,8):
					if click(x,x+6,y,y+6):
						for i in range(9):
							if data[i][1]==(x,y) and data[i][2]==0:
								window.blit(P1 if J==1 else P2,(x*15,y*15))
								data[i][2]=J
								J=1 if J==2 else 2
								for u in combination:
									for v in range(3):
										for w in range(9):
											if u[v]==data[w][0]:
												vars()['abc'[v]]=data[w][2]
									if a*b*c==1 or a*b*c==8:
										window.blit(W1 if a*b*c==1 else W2,(0,0))
										pygame.display.flip()
										reset=True

	pygame.display.flip()