def func(*args):
	ret_values = []
	
	(n, k) = (int(i) for i in args[0].split())
	if (n == 1):
	    ret_values.append(0)
	    exit()
	if (k >= int((n / 2))):
	    t = ((n * (n - 1)) / 2)
	    ret_values.append(int(t))
	    exit()
	s = (n - (2 * k))
	p = ((s * (s - 1)) / 2)
	l = ((n * (n - 1)) / 2)
	output = (l - p)
	ret_values.append(int(output))

	return ret_values
