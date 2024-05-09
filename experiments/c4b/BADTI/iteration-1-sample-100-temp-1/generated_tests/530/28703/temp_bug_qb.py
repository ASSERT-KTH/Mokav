def original_func(*args):
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
	diva = (n // a)
	divb = (n // b)
	divab = (n // (a * b))
	if (m == p):
	    global_list.append(((diva * p) + ((divb - divab) * q)))
	else:
	    global_list.append(((divb * q) + ((diva - divab) * p)))
	return global_list