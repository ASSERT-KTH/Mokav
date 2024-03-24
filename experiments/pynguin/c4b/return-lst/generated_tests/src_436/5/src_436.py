def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	l = (a // k)
	p = (b // k)
	if (l == 0):
	    if ((b % k) == 0):
	        if ((l + p) != 0):
	            ret_values.append((l + p))
	        else:
	            ret_values.append('-1')
	    else:
	        ret_values.append('-1')
	elif (p == 0):
	    if ((a % k) == 0):
	        if ((l + p) != 0):
	            ret_values.append((l + p))
	        else:
	            ret_values.append('-1')
	    else:
	        ret_values.append('-1')
	else:
	    ret_values.append((l + p))

	return ret_values
