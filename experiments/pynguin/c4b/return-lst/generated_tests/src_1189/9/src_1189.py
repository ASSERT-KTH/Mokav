def func(*args):
	ret_values = []
	
	import math
	a = list(map(int, args[0].split()))
	a.sort()
	ret_values.append((abs((a[1] - a[0])) + abs((a[1] - a[2]))))

	return ret_values
