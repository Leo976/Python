import os

square=[[0,0,0],[0,0,0],[0,0,0]]
win=((5,6,7),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1))

def key(x):
	y=int(x/3)
	x=x%3
	if x==0:
		x=3
		y-=1
	return [x-1,2-y]

def end():
	for a in range(8):
		produit=1
		for b in range(3):
			case=key(win[a][b])
			produit=produit*square[case[1]][case[0]]
		if produit==8 or produit==1:
			print(player2 if produit==8 else player1, 'a gagné la partie !')
			return False
	return True

def replay():
	try:
		a=int(input('Pour rejouer entrez le chiffre 1...\n'))
		if a==1:
			return True
		else:
			print('À bientôt !')
			return False
	except:
		print('À bientôt !')
		return False

boucle=True
player1=input('Entrez votre nom joueur 1 >> ')
player2=input('Entrez votre nom joueur 2 >> ')
player=1

while boucle:
	
	os.system('cls')
	for i in range(3):
		print(square[i][0],'|',square[i][1],'|',square[i][2])

	print('Au tour de {0} de jouer !'.format(player1 if player==1 else player2))

	case=False
	while not(case):
		try:
			case=key(int(input('Entrez une case >> ')))
			if  square[case[1]][case[0]]>0:
				print('Case déjà prise !')
				case=False
		except:
			print('Merci d\'entrer un chiffre entre 1 et 9 !')
			case=False

	square[case[1]][case[0]]=player
	player=1 if player==2 else 2

	boucle=end()

	produit=1
	for y in range(3):
		for x in range(3):
			produit=produit*square[y][x]

	if produit!=0:
		print('Égalité !')
		boucle=replay()

	if not(boucle):
		if replay():
			boucle=True
			square=[[0,0,0],[0,0,0],[0,0,0]]
			player1=input('Entrez votre nom joueur 1 >> ')
			player2=input('Entrez votre nom joueur 2 >> ')
			player=1