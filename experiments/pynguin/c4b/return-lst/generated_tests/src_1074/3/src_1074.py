def func(*args):
	ret_values = []
	
	import math
	(a, b) = args[0].split()
	(a, b) = (int(a), int(b))
	p = ((2 * math.floor(math.sqrt(a))) + 1)
	q = (math.floor(math.sqrt((1 + (4 * b)))) + 1)
	if (p < q):
	    ret_values.append('Vladik')
	else:
	    ret_values.append('Valera')

	return ret_values
