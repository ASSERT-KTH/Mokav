def func(*args):
	ret_values = []
	
	(*m, d) = (int(args[0]) for i in range(5))
	ret_values.append(sum(((1 - all((((i + 1) % k) for k in m))) for i in range(d))))

	return ret_values
