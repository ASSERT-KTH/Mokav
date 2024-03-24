def func(*args):
	ret_values = []
	
	n = int(args[0])
	e = ((10 ** 9) + 7)
	ret_values.append((1 if (n == 0) else ((pow(2, (n - 1), e) + pow(2, ((n * 2) - 1), e)) % e)))

	return ret_values
