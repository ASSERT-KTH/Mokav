def func(*args):
	
	import math
	n = int(args[0])
	ans = 0
	for x in range(1, n):
	    ans += (x * (n - x))
	ans += n
	return(ans)
