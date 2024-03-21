def func(*args):
	ret_values = []
	
	import math
	rows = [0, 1, 0, 1]
	seats = ['f', 'e', 'd', 'a', 'b', 'c']
	s = args[0]
	(a, b) = (int(s[:(- 1)]), s[(- 1)])
	ret_values.append(((((((a - 1) // 4) * 16) + (rows[((a % 4) - 1)] * 7)) + seats.index(b)) + 1))

	return ret_values
