def func(*args):
	ret_values = []
	
	import math
	(n, k) = map(int, args[0].split())
	i = 2
	while True:
	    if ((k % i) == (i // 2)):
	        ans = (math.log2((i // 2)) + 1)
	        ret_values.append(int(ans))
	        exit()
	    i *= 2

	return ret_values
