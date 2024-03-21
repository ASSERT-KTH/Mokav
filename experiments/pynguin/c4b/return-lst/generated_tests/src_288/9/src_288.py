def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = 0
	p = 2
	if (n == 1):
	    ret_values.append(1)
	elif (n == 2):
	    ret_values.append(3)
	elif (n > 2):
	    for i in range((n - 2), 0, (- 1)):
	        m += ((i * p) + 1)
	        p += 1
	    ret_values.append(((n + m) + 1))

	return ret_values
