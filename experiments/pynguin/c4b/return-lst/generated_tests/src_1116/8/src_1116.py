def func(*args):
	ret_values = []
	
	(n, m) = list(map(int, args[0].split()))
	c = 0
	for a in range(1000):
	    for b in range(1000):
	        if ((((a * a) + b) == n) and ((a + (b * b)) == m)):
	            c += 1
	ret_values.append(c)

	return ret_values
