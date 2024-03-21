def func(*args):
	ret_values = []
	
	(m, n, a) = (int(x) for x in args[0].split())
	if (((m % a) == 0) and ((n % a) == 0)):
	    ret_values.append(int((int((m / a)) * int((n / a)))))
	if (((m % a) > 0) and ((n % a) == 0)):
	    ret_values.append((int(((m / a) + 1)) * int((n / a))))
	if (((m % a) == 0) and ((n % a) > 0)):
	    ret_values.append((int((m / a)) * int(((n / a) + 1))))
	if (((m % a) > 0) and ((n % a) > 0)):
	    ret_values.append((int(((m / a) + 1)) * int(((n / a) + 1))))

	return ret_values
