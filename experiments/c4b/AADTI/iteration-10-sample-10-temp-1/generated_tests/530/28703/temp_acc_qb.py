def patched_func(*args):
	global_list = []
	
	liste = args[0].split(' ')
	n = int(liste[0])
	a = int(liste[1])
	b = int(liste[2])
	p = int(liste[3])
	q = int(liste[4])
	m = max(p, q)
	res = 0
	multa = a
	multb = b
	
	def pgcd(a, b):
	    "pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"
	    while (b != 0):
	        (a, b) = (b, (a % b))
	    return a
	ppcm = ((a * b) / pgcd(a, b))
	diva = (n // a)
	divb = (n // b)
	divab = int((n // ppcm))
	if (m == p):
	    global_list.append(((diva * p) + ((divb - divab) * q)))
	else:
	    global_list.append(((divb * q) + ((diva - divab) * p)))
	return global_list