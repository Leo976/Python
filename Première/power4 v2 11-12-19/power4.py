import pygame,time,itertools
from pygame.locals import *

pygame.init()
window=pygame.display.set_mode((590,690),pygame.DOUBLEBUF)
pygame.display.set_caption('Power4 v.2')

for i in ('fond','P0','P1','P2','W0','W1','W2','point'):
	vars()[i]=pygame.image.load('images/{}.png'.format(i))

def display(win,winner,curseur):
	window.blit(fond,(0,0))
	for x,y in itertools.product(range(7),range(6)):
		if cases[y][x]>0:
			window.blit(P1 if cases[y][x]==1 else P2,((5+x*7)*10,(22+y*7)*10))
	for x,a in {230:20,350:-20}.items():
		for i in range(score[0 if x!=350 else 1]):
			window.blit(point,(x,70))
			x+=a
	if win:
		window.blit([W0,W1,W2][winner],(230,150))
		pygame.display.flip()
		time.sleep(4)
		score[winner-1]+=0 if winner==0 else 1
		return [[0 for i in range(7)] for i in range(6)]
	if curseur:
		window.blit(P1 if PX==1 else P2,(x_mouse[0],140))
	pygame.display.flip()
	return cases
def animation(y):
	for i in range(y):
		window.blit(fond,(0,0))
		display(False,0,False)
		window.blit(P1 if PX==1 else P2,(x_mouse[0],220+i*70))
		pygame.display.flip()
		time.sleep(1/16)
def win_check():
	for y,x,i in itertools.product(range(6),range(4),range(4)):
		u=1 if i==0 else u
		u=cases[y][x+i]*u
		if (u==1 or u==16) and i==3:
			return display(True,2 if u==16 else u,True)
	for x,y,i in itertools.product(range(7),range(3),range(4)):
		u=1 if i==0 else u
		u=cases[y+i][x]*u
		if (u==1 or u==16) and i==3:
			return display(True,2 if u==16 else u,True)
	for n in range(24):
		x=int(diagonal[n][0])
		y=int(diagonal[n][1])
		u=1
		for i in range(4):
			u=cases[y][x]*u
			x+=1 if n<12 else -1
			y+=1
		if u==1 or u==16:
			return display(True,2 if u==16 else u,True)
	for x,y in itertools.product(range(7),range(6)):
		if cases[y][x]==0:
			return cases
	return display(True,0,True)
def mouse_range(x1,y1,x2,grill):
	for i in range(x1,x1+(x2-x1)*6+1,(x2-x1)):
		if i<=pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0]<=i+(x2-x1)-grill:
			return (i,int(i/70))
	return x_mouse

dgnl_1,dgnl_2=list(),list()
for x,y in itertools.product(range(4),range(3)):
	dgnl_1.append(str(x)+str(y))
for x,y in itertools.product(range(3,7),range(3)):
	dgnl_2.append(str(x)+str(y))
diagonal=dgnl_1+dgnl_2

score=[0,0]
cases=[[0 for i in range(7)] for i in range(6)]
PX=1
x_mouse=(260,3)

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()

		x_mouse=mouse_range(50,220,120,10)

		if event.type==MOUSEBUTTONDOWN and event.button==1:
			boucle=True
			for y in range(5,-1,-1):
				if cases[y][x_mouse[1]]==0 and boucle:
					boucle=False
					animation(y)
					cases[y][x_mouse[1]]=PX
					cases=win_check()
					PX=1 if PX==2 else 2

		if score[0]==3 or score[1]==3:
			score=[0,0]

	cases=win_check()
	cases=display(False,0,True)