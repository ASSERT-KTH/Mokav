def func(*args):
	ret_values = []
	
	(y, k, n) = map(int, args[0].split(' '))
	lst = []
	x = (k - (y % k))
	while ((x + y) <= n):
	    if (((x + y) % k) == 0):
	        lst.append(x)
	    x += k
	if (len(lst) == 0):
	    ret_values.append((- 1))
	else:
	    ret_values.append(' '.join(list(map(str, lst))))

	return ret_values
