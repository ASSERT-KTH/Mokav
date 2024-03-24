def func(*args):
	ret_values = []
	
	(a, b) = args[0].split(' ')
	a = int(a)
	b = int(b)
	c = 0
	while ((a > 0) and (b > 0) and ((a + b) > 2)):
	    if (a < b):
	        a += 1
	        b -= 2
	    else:
	        a -= 2
	        b += 1
	    c += 1
	ret_values.append(c)

	return ret_values
