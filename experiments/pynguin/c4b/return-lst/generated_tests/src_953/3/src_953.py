def func(*args):
	ret_values = []
	
	(n, k) = [int(i) for i in args[0].split()]
	ans = 0
	for i in range(k):
	    if (n >= 2):
	        ans += ((2 * n) - 3)
	        n -= 2
	ret_values.append(ans)

	return ret_values
