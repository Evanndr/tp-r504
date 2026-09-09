import fonctions as f
print("Hello, World!")


def carre(chiffre):
	return int(chiffre)**2

while True:
	chiffre = input("Choisir un nombre pour avoir son carré. ")
	print(carre(chiffre))
	a = input("Choisir un nombre a. ")
	b = input("Choisir un nombre b. ")
	res = f.puissance(a,b)
	print(res)
