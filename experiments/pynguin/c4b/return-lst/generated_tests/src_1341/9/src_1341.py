def func(*args):
	ret_values = []
	
	ns = args[0]
	n = int(ns[:(- 1)])
	s = ns[(len(ns) - 1)]
	r = (n - 1)
	if (((n % 4) == 0) or (((n + 1) % 4) == 0)):
	    d = ((n // 2) - 1)
	    r = (n - 3)
	else:
	    d = (n // 2)
	t = ((d * 6) + r)
	if (s == 'f'):
	    t += 1
	elif (s == 'e'):
	    t += 2
	elif (s == 'd'):
	    t += 3
	elif (s == 'a'):
	    t += 4
	elif (s == 'b'):
	    t += 5
	elif (s == 'c'):
	    t += 6
	ret_values.append(t)

	return ret_values
