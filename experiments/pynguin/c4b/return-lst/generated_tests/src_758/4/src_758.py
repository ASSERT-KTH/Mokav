def func(*args):
	ret_values = []
	
	(n, a, b, c) = [int(args[0]) for _ in '1234']
	r = 0
	if ((b - c) < a):
	    r = ((n // (b - c)) - (b // (b - c)))
	    if (r < 0):
	        r = 0
	    n -= (r * (b - c))
	    while (b <= n):
	        t = (n // b)
	        r += t
	        n = ((n % b) + (t * c))
	ret_values.append((r + (n // a)))

	return ret_values
