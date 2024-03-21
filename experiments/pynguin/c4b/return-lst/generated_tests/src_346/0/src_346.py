def func(*args):
	ret_values = []
	
	from math import gcd
	(a, b, n) = map(int, args[0].split())
	ans = 1
	while True:
	    if (ans == 1):
	        x = gcd(a, n)
	    else:
	        x = gcd(b, n)
	    if (n < x):
	        ret_values.append(ans)
	        exit()
	    n -= x
	    ans = (1 if (ans == 0) else 0)

	return ret_values
