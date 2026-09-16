def puissance(a, b):
	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")
		if b < 0:
			raise TypeError("opération d’élevation de puissance indéfinie")
	for i in range(b):
		a = a*a
    if b < 0:
        return 1 / resultat

	return a

