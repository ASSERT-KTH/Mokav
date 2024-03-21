def func(*args):
	ret_values = []
	
	(n, a) = map(int, args[0].split())
	i = 1
	c = 0
	if ((a % 2) != 0):
	    while (i != a):
	        c = (c + 1)
	        i += 2
	    ret_values.append((c + 1))
	i = n
	if ((a % 2) == 0):
	    while (i != a):
	        c += 1
	        i -= 2
	    ret_values.append((c + 1))

	return ret_values
