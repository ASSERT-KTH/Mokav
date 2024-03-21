def func(*args):
	ret_values = []
	
	from math import sqrt
	(a, b, c) = map(int, args[0].split())
	s = int(sqrt(((a * b) * c)))
	ret_values.append(((((s // a) + (s // b)) + (s // c)) * 4))

	return ret_values
