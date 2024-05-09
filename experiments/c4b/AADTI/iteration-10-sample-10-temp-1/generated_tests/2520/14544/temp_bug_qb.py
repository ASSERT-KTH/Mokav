def original_func(*args):
	global_list = []
	
	from fractions import Fraction
	(x, y) = map(int, args[0].split())
	m = max(x, y)
	n = (7 - m)
	r = (n / 6)
	res = Fraction(r)
	global_list.append(('%d%s%d' % (res.numerator, '/', res.denominator)))
	return global_list