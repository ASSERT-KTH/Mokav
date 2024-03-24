def func(*args):
	ret_values = []
	
	(a, b) = list(map(int, args[0].split()))
	d1 = int((a ** 0.5))
	d2 = int(((((1 + (4 * b)) ** 0.5) - 1) / 2))
	if (d1 > d2):
	    ret_values.append('Valera')
	else:
	    ret_values.append('Vladik')

	return ret_values
