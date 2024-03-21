def func(*args):
	ret_values = []
	
	x = args[0]
	n = (int(x[:(- 1)]) - 1)
	s = [4, 5, 6, 3, 2, 1][(ord(x[(- 1)]) - ord('a'))]
	ret_values.append(((((n // 4) * 16) + ((n % 2) * 7)) + s))

	return ret_values
