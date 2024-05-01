def original_func(*args):
	global_list = []
	
	'input\n6 11 6\n'
	from math import gcd
	(a, b, c) = map(int, args[0].split())
	global_list.append(('Yes' if ((c % gcd(a, b)) == 0) else 'No'))
	return global_list