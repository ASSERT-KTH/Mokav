def func(*args):
	ret_values = []
	
	import math
	l = [int(x) for x in str(args[0]).split(' ')]
	n = l[0]
	m = l[1]
	if (m >= n):
	    ret_values.append(n)
	else:
	    a = (1 + (8 * (n - m)))
	    b = int(math.sqrt(a))
	    if ((b * b) < a):
	        b = (b + 1)
	    ret_values.append((m + math.ceil(((b / 2) - 0.5))))

	return ret_values
