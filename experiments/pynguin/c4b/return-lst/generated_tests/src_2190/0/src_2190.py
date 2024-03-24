def func(*args):
	ret_values = []
	
	(n, m) = args[0].split()
	n = int(n)
	m = int(m)
	c = 0
	for a in range((max(n, m) + 1)):
	    for b in range((max(n, m) + 1)):
	        if ((((a ** 2) + b) == n) and ((a + (b ** 2)) == m)):
	            c = (c + 1)
	ret_values.append(c)

	return ret_values
