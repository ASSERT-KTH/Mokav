def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	i = int(math.log(math.ceil(((n * 1.0) / 5)), 2))
	ind = math.ceil(((n - (((2 ** i) - 1) * 5)) / (2 ** i)))
	ret_values.append(names[(ind - 1)])

	return ret_values
