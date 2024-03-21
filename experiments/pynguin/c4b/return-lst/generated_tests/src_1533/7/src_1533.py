def func(*args):
	ret_values = []
	
	(m, n) = map(int, args[0].split(' '))
	if ((m % 2) == 0):
	    ret_values.append(((m // 2) * n))
	else:
	    suma = ((m // 2) * n)
	    c = n
	    d = 1
	    suma += ((c // 2) * d)
	    ret_values.append(suma)

	return ret_values
