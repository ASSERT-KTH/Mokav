def original_func(*args):
	global_list = []
	
	import math
	(a, b) = args[0].split()
	(a, b) = (int(a), int(b))
	p = ((2 * math.floor(math.sqrt(a))) + 1)
	q = (math.floor(math.sqrt((1 + (4 * b)))) - 1)
	if (p < q):
	    global_list.append('Vladik')
	else:
	    global_list.append('Valera')
	return global_list