def func(*args):
	ret_values = []
	
	from fractions import Fraction
	(y, w) = map(int, args[0].split())
	a = ((6 - max(y, w)) + 1)
	b = 6
	if (a == 6):
	    ret_values.append('1/1')
	else:
	    ret_values.append(Fraction(a, b))

	return ret_values
