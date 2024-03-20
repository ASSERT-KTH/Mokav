def func(*args):
	
	import math
	n = int(args[0])
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	i = int(math.log(math.ceil(((n * 1.0) / 5)), 2))
	ind = math.ceil(((n - (((2 ** i) - 1) * 5)) / (2 ** i)))
	return(names[(ind - 1)])
