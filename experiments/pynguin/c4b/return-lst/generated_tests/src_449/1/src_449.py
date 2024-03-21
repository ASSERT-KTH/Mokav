def func(*args):
	ret_values = []
	
	(k, r) = map(int, args[0].split())
	ret_values.append(min((i for i in range(1, 11) if ((((k * i) % 10) == r) or (((k * i) % 10) == 0)))))

	return ret_values
