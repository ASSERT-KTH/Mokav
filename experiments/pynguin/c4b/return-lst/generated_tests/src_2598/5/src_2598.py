def func(*args):
	ret_values = []
	
	ab = args[0]
	a = int(ab.split(' ')[0])
	b = int(ab.split(' ')[1])
	a1 = int((a ** (1 / 2)))
	b1 = int((((((4 * b) + 1) ** (1 / 2)) - 1) / 2))
	if ((a1 - b1) >= 1):
	    ret_values.append('Valera')
	else:
	    ret_values.append('Vladik')

	return ret_values
