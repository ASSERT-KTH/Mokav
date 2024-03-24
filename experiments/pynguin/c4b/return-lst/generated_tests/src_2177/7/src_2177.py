def func(*args):
	ret_values = []
	
	from functools import reduce
	from operator import mul
	c = list(map(int, args[0].split()))
	(r, h) = (reduce(mul, c[1::2], 1), reduce(mul, c[0::2], 1))
	rw = ((r > h) or ((c[2] == 0) and (c[3] != 0)) or ((c[0] == 0) and ((c[1] * c[3]) != 0)))
	ret_values.append(('Ron' if rw else 'Hermione'))

	return ret_values
