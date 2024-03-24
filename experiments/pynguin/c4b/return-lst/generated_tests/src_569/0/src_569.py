def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split())
	if (b > 0):
	    b = round((b % n))
	    if ((a + b) > n):
	        ret_values.append(((a + b) - n))
	    else:
	        ret_values.append((a + b))
	elif (b == 0):
	    ret_values.append(a)
	else:
	    b = round((abs(b) % n))
	    if ((b - a) < 0):
	        ret_values.append((a - b))
	    elif ((a - b) == 0):
	        ret_values.append(n)
	    else:
	        ret_values.append((n - (b - a)))

	return ret_values
