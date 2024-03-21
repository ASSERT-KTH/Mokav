def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	ret_values.append(max(abs((a - c)), abs((d - b))))

	return ret_values
