def original_func(*args):
	global_list = []
	
	(a, b, c, d, e, f) = map(int, args[0].split())
	if (((((a * c) * e) == 0) and ((f > 0) or (d > 0))) or (((b * d) * f) > ((a * c) * e) > 0)):
	    global_list.append('Ron')
	else:
	    global_list.append('Hermione')
	return global_list