def func(*args):
	ret_values = []
	
	from math import factorial
	ret_values.append(factorial(min(map(int, args[0].split(' ')))))

	return ret_values
