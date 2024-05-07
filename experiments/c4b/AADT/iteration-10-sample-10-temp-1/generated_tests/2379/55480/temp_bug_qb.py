def original_func(*args):
	global_list = []
	
	(a, b, c, d, e, f) = map(int, args[0].split())
	global_list.append(('Ron' if ((((a * e) * c) < ((f * d) * b)) or ((not c) and d) or ((not a) and b and (not d))) else 'Hermione'))
	return global_list