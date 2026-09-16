def puissance(a, b):
	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")
	exposant = abs(b)
	resultat = 1
	for i in range(exposant):
		resultat = resultat * a 
	if b < 0:
 		return 1 / resultat
	return resultat

