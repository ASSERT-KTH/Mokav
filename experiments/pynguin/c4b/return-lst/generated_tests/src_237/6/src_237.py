def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	ans = 0
	for x in range(1, n):
	    ans += (x * (n - x))
	ans += n
	ret_values.append(ans)

	return ret_values
