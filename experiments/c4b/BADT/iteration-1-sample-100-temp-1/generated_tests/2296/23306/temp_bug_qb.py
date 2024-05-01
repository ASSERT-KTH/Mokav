def original_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split(' '))
	if ((m % 2) == 0):
	    global_list.append(((m // 2) * n))
	else:
	    suma = ((m // 2) * n)
	    a = m
	    m = 1
	    n = a
	    suma += ((n // 2) * m)
	    global_list.append(suma)
	return global_list