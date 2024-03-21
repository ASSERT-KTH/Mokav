def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	z = ([0] + ([(- 1000000000.0)] * 5000))
	for i in range(1, (n + 1)):
	    z[i] = (max(z[(i - a)], z[(i - b)], z[(i - c)]) + 1)
	ret_values.append(z[n])

	return ret_values
