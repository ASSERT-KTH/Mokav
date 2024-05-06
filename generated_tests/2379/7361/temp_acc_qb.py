def patched_func(*args):
	global_list = []
	
	(a, b, c, d, e, f) = map(int, args[0].split())
	if ((((a * e) * c) < ((f * d) * b)) or ((c == 0) and d) or ((a == 0) and b and d)):
	    global_list.append('Ron')
	else:
	    global_list.append('Hermione')
	return global_list