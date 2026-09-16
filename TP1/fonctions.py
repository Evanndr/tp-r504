def puissance(a, b):
	if not isinstance(a, int) or not isinstance(b, int):
		raise TypeError("Only integers are allowed")
	if a == 0 and b == 0:
		raise Exception("Sorry, no numbers below zero")
	exposant = abs(b)
	resultat = 1
	for i in range(exposant):
		resultat = resultat * a 

	if b < 0:
		return 1 / resultat
	return resultat




