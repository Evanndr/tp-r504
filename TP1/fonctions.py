def puissance(a, b):
	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")
	if b < 0:
		raise Exception("Sorry, no numbers below zero")
	if a == 0:
		raise Exception("Sorry, no numbers below zero")
	exposant = abs(b)
	resultat = 1
	for i in range(exposant):
		resultat = resultat * a 
	return resultat




