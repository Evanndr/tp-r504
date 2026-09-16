def puissance(a, b):

	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")

    # Traiter le cas de l'exposant négatif pour la boucle range
	exposant = abs(b)
	resultat = 1
    
    # On multiplie 'resultat' par 'a', exactement 'exposant' fois
	for i in range(exposant):
		resultat = resultat * a     # Et NON PAS a = a * a
        
    # Si l'exposant était négatif, on applique l'inversion
	if b < 0:
 		return 1 / resultat
        
	return resultat

