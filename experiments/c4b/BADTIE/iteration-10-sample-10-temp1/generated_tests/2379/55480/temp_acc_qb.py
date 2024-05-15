def patched_func(*args):
	global_list = []
	
	(a, b, c, d, e, f) = map(int, args[0].split())
	global_list.append(('Ron' if ((((a * e) * c) < ((f * d) * b)) or ((c == 0) and d) or ((a == 0) and b and d)) else 'Hermione'))
	return global_list