def func(*args):
	
	import math
	(n, k, p) = map(int, args[0].split())
	need = math.ceil(((n * p) / 100))
	res = (need - k)
	return((res if (res > 0) else 0))
