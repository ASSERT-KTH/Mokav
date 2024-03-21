def func(*args):
	ret_values = []
	
	n = int(args[0])
	while ((n % 2) == 0):
	    ret_values.append(n, end=' ')
	    n //= 2
	for x in range(3, (int((n ** 0.5)) + 1), 2):
	    while ((n % x) == 0):
	        ret_values.append(n, end=' ')
	        n //= x
	if (n != 1):
	    ret_values.append(n, 1)
	else:
	    ret_values.append(1)

	return ret_values
