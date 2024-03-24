def func(*args):
	ret_values = []
	
	'input\n6 11 6\n'
	from math import gcd
	(a, b, c) = map(int, args[0].split())
	for x in range(((c // a) + 1)):
	    if (((c - (x * a)) % b) == 0):
	        ret_values.append('Yes')
	        break
	else:
	    ret_values.append('No')

	return ret_values
