def func(*args):
	ret_values = []
	
	'input\n24648817341102 41165114064236 88046848035 13602161452932 10000831349205\n'
	(l1, r1, l2, r2, k) = map(int, args[0].split())
	l = max(l1, l2)
	r = min(r1, r2)
	if (l > r):
	    ret_values.append(0)
	else:
	    ret_values.append((((r - l) + 1) if ((k < l) or (k > r)) else (r - l)))

	return ret_values
