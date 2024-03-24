def func(*args):
	ret_values = []
	
	(a, b) = (int(i) for i in args[0].split())
	t = 0
	if (a > b):
	    (a, b) = (b, a)
	if (b < 2):
	    ret_values.append(0)
	else:
	    while (b > 2):
	        x = ((b - 1) // 2)
	        t += x
	        a += x
	        b -= (2 * x)
	        (a, b) = (b, a)
	    ret_values.append((t + 1))

	return ret_values
