def patched_func(*args):
	global_list = []
	
	'input\n2 3 4\n'
	(a, b, c) = sorted(map(int, args[0].split()))
	global_list.append(((((b + a) - 1) * ((c + a) - 1)) - (a * (a - 1))))
	return global_list