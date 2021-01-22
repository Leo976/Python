import pygame
from pygame.locals import *
#initialise la surface..
pygame.init()
#initialise la surface en (x,y) dans la var window..
window=pygame.display.set_mode((300,300))
case=pygame.image.load('case.png').convert()
#.blit >> colle l'image dans window..
window.blit(case,(0,0))
#.convert_alpha >> retire la transparence..
J1=pygame.image.load('player1.png').convert_alpha()
J2=pygame.image.load('player2.png').convert_alpha()
win1=pygame.image.load('win1.png').convert_alpha()
win2=pygame.image.load('win2.png').convert_alpha()
#data==[key,(x,y),J] >> [[1,(2,20),0],[2,(11,20),0],[3,(20,20),0]...[9,(20,2),0]]
data=list()
key=1
for y in range(20,1,-9):
	for x in range(2,21,9):
		data.append([key,(x,y),0])
		key+=1
combination=((7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1))
def click(x1,x2,y1,y2):
	return event.pos[0]>=x1*10 and event.pos[0]<=x2*10 and event.pos[1]>=y1*10 and event.pos[1]<=y2*10
J=1
while True:
	for event in pygame.event.get():#...?
		#permet de quitter avec la croix rouge..
		if event.type==pygame.QUIT:
			pygame.quit()
		#si clique sur le bouton gauche (1)..
		if event.type==MOUSEBUTTONDOWN and event.button==1:
			for y in range(2,21,9):
				for x in range(2,21,9):
					#si clique souris est entre x1,x2 et y1,y2..
					if click(x,x+8,y,y+8):
						for i in range(9):
							#si J==0..
							if data[i][1]==(x,y) and data[i][2]==0:
								window.blit(J1 if J==1 else J2,(x*10,y*10))
								data[i][2]=J
								J=1 if J==2 else 2
								#complexe à expliquer il faut une feuille x)
								for u in combination:
									a=0
									b=0
									c=0
									for w in range(9):
										if u[0]==data[w][0]:
											a=data[w][2]
									for w in range(9):
										if u[1]==data[w][0]:
											b=data[w][2]
									for w in range(9):
										if u[2]==data[w][0]:
											c=data[w][2]
									if a*b*c==1:
										print('Joueur 1 gagne !')
										window.blit(win1,(0,0))
										pygame.display.flip()
										while True:
											if event.type==MOUSEBUTTONDOWN and event.button==1:
												pygame.quit()
									elif a*b*c==8:
										print('Joueur 2 gagne !')
										window.blit(win2,(0,0))
										pygame.display.flip()
										while True:
											if event.type==MOUSEBUTTONDOWN and event.button==1:
												pygame.quit()
									#print(u,a,b,c)
	#pour rafraîchir l'image..
	pygame.display.flip()