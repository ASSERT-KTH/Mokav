def func(*args):
	ret_values = []
	
	n = args[0]
	t = ((((n[0] + n[2]) + n[4]) + n[3]) + n[1])
	t = int(t)
	k = t
	for i in range(2):
	    t = ((t ** 2) % (10 ** 5))
	m = ((k * t) % (10 ** 5))
	ret_values.append((('0' * (5 - len(str(m)))) + str(m)))

	return ret_values
