def func(*args):
	ret_values = []
	
	(t, s, x) = map(int, args[0].split())
	if (x >= t):
	    if ((t + s) <= x):
	        y1 = ((x - t) / s)
	        y2 = (((x - t) - 1) / s)
	        if (int(y1) == y1):
	            ret_values.append('YES')
	        elif (int(y2) == y2):
	            ret_values.append('YES')
	        else:
	            ret_values.append('NO')
	    elif (x == t):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
