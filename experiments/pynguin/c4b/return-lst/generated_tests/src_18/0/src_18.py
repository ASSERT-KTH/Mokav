def func(*args):
	ret_values = []
	
	x = list(map(int, args[0].strip().split()))
	ret_values.append(abs((min(x) - max(x))))

	return ret_values
