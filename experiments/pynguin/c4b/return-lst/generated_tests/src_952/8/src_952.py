def func(*args):
	ret_values = []
	
	(n, m) = [int(i) for i in args[0].split()]
	if ((n % 2) == 1):
	    if (m >= ((n - 1) / 2)):
	        ret_values.append(int((((n - 1) * n) / 2)))
	    else:
	        t = (((n - 1) / 2) - m)
	        ret_values.append(int(((((n - 1) * n) / 2) - (t * ((t * 2) + 1)))))
	elif (m >= (n / 2)):
	    ret_values.append(int((((n - 1) * n) / 2)))
	else:
	    t = ((n / 2) - m)
	    ret_values.append(int(((((n - 1) * n) / 2) - (t * ((t * 2) - 1)))))

	return ret_values
