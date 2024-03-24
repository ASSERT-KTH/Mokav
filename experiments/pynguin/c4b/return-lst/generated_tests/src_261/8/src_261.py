def func(*args):
	ret_values = []
	
	n = int(args[0])
	ti = 1
	if (n <= 2):
	    ret_values.append((- 1))
	    exit(0)
	n -= 2
	ti = (10 ** n)
	if (ti % 21):
	    ti //= 21
	    ti += 1
	    ti *= 21
	ti *= 10
	ret_values.append(ti)

	return ret_values
