def func(*args):
	ret_values = []
	
	(l, r, k) = map(int, args[0].split())
	l1 = []
	k1 = 1
	while (k1 <= r):
	    if (k1 >= l):
	        l1.append(k1)
	    k1 = (k1 * k)
	if (len(l1) == 0):
	    ret_values.append((- 1))
	else:
	    ret_values.append(*l1)

	return ret_values
