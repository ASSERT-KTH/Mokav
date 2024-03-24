def func(*args):
	ret_values = []
	
	(l, r, k) = map(int, args[0].split())
	s = ''
	for i in range(500):
	    if (((k ** i) <= r) and ((k ** i) >= l)):
	        s += (str((k ** i)) + ' ')
	if (len(s) > 0):
	    ret_values.append(s)
	else:
	    ret_values.append((- 1))

	return ret_values
