def func(*args):
	ret_values = []
	
	(n, a, b) = (int(i) for i in args[0].split())
	c = (abs(b) % n)
	if (b < 0):
	    r = (a - c)
	    if (r < 1):
	        r += n
	else:
	    r = (a + c)
	    if (r > n):
	        r -= n
	ret_values.append(r)

	return ret_values
