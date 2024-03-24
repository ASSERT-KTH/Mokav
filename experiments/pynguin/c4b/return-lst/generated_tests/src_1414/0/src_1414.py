def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	z = 0
	for x in range(n):
	    z += ((m + ((x + 1) % 5)) // 5)
	ret_values.append(z)

	return ret_values
