def func(*args):
	ret_values = []
	
	'input\n1 11\n'
	(n, m) = map(int, args[0].split())
	t = 0
	for a in range(10000):
	    if (((((a + (n ** 2)) - ((2 * n) * (a ** 2))) + (a ** 4)) == m) and ((n - (a ** 2)) >= 0)):
	        t += 1
	ret_values.append(t)

	return ret_values
