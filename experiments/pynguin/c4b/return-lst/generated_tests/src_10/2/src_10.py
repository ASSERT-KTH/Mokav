def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	if ((c == 0) and (a == b)):
	    exit(ret_values.append('YES'))
	elif ((c == 0) and (a != b)):
	    exit(ret_values.append('NO'))
	(l, r) = (0, (2 * (10 ** 9)))
	while (l <= r):
	    mid = ((l + r) // 2)
	    s = (a + (mid * c))
	    if (s == b):
	        exit(ret_values.append('YES'))
	    elif (s > b):
	        if (c > 0):
	            r = (mid - 1)
	        else:
	            l = (mid + 1)
	    elif (c > 0):
	        l = (mid + 1)
	    else:
	        r = (mid - 1)
	ret_values.append('NO')

	return ret_values
