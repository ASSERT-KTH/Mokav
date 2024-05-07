def original_func(*args):
	global_list = []
	
	(m, n) = [int(x) for x in args[0].split()]
	a = ((m * (n // 2)) + ((m // 2) * (m % 2)))
	b = ((n * (m // 2)) + ((n // 2) * (n % 2)))
	global_list.append(max(a, b))
	return global_list