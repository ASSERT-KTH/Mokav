def func(*args):
	
	import math
	a = list(map(int, args[0].split()))
	a.sort()
	return((abs((a[1] - a[0])) + abs((a[1] - a[2]))))
