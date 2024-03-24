def func(*args):
	ret_values = []
	
	n = int(args[0])
	for i in range(2, (10 ** 6)):
	    while ((n % (i ** 2)) == 0):
	        n = (n // i)
	ret_values.append(n)

	return ret_values
