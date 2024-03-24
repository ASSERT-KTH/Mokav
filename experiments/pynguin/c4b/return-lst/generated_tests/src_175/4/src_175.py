def func(*args):
	ret_values = []
	
	(l1, r1, l2, r2, k) = map(int, args[0].split())
	if ((l1 > r2) or (r1 < l2)):
	    ret_values.append(0)
	    quit()
	t = (max((min(r1, r2) - max(l1, l2)), 0) + 1)
	if (((k >= l2) and (k <= r2)) and ((k >= l1) and (k <= r1))):
	    t -= 1
	ret_values.append(t)

	return ret_values
