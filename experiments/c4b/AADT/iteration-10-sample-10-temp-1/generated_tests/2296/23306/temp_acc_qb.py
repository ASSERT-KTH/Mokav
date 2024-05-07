def patched_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split(' '))
	if ((m % 2) == 0):
	    global_list.append(((m // 2) * n))
	else:
	    suma = ((m // 2) * n)
	    c = n
	    d = 1
	    suma += ((c // 2) * d)
	    global_list.append(suma)
	return global_list