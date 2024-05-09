def original_func(*args):
	global_list = []
	
	'input\n4 6 6\n'
	
	def gcd(x, y):
	    while (y != 0):
	        (x, y) = (y, (x % y))
	    return x
	(a, b, c) = map(int, args[0].split())
	l = ((a * b) // gcd(a, b))
	l = ((l * c) // gcd(l, c))
	x = (((l // a) + (l // b)) + (l // c))
	if (len(set([a, b, c])) < 3):
	    global_list.append((4 * x))
	else:
	    global_list.append((8 * x))
	return global_list