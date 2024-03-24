def func(*args):
	ret_values = []
	
	import math
	(n, k, p) = map(int, args[0].split())
	need = math.ceil(((n * p) / 100))
	res = (need - k)
	ret_values.append((res if (res > 0) else 0))

	return ret_values
