def func(*args):
	ret_values = []
	
	(n, k) = (int(x) for x in args[0].split())
	time = (240 - k)
	r = 0
	while ((time >= 0) and (r <= n)):
	    r += 1
	    time -= (5 * r)
	ret_values.append((r - 1))

	return ret_values
