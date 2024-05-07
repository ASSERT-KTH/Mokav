def patched_func(*args):
	global_list = []
	
	import math
	string = args[0]
	numbers = string.split()
	x = int(numbers[0])
	y = int(numbers[1])
	a = ((6 - max([x, y])) + 1)
	b = 6
	n = math.gcd(a, b)
	a /= n
	b /= n
	global_list.append(('%d/%d' % (a, b)))
	return global_list