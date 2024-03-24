def func(*args):
	
	n = int(args[0])
	a = int(args[1])
	b = int(args[2])
	c = int(args[3])
	d = (b - c)
	count = 0
	if ((a <= d) or ((a <= n) and (b > n))):
	    count = (n // a)
	elif (n >= b):
	    (count, _) = divmod((n - c), d)
	    count += ((n - (count * d)) // a)
	return(count)
