def patched_func(*args):
	global_list = []
	
	from fractions import Fraction
	(y, w) = map(int, args[0].split())
	a = ((6 - max(y, w)) + 1)
	b = 6
	if (a == 6):
	    global_list.append('1/1')
	else:
	    global_list.append(Fraction(a, b))
	return global_list