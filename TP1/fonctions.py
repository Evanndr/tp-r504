def puissance(a, b):

	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")

    # Gestion du cas particulier de l'exposant nul
    if b == 0:
        return 1
    
    # On travaille d'abord avec la valeur absolue de l'exposant
    exposant_positif = abs(b)
    resultat = 1
    
    # Boucle pour multiplier 'a', 'b' fois
    for _ in range(exposant_positif):
        resultat = resultat * a
        
    # Si l'exposant de départ était négatif, on inverse le résultat
    if b < 0:
        return 1 / resultat
        
    return resultat


