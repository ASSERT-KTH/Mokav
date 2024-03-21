def func(*args):
	ret_values = []
	
	(m, n) = map(int, args[0].split(' '))
	if ((n == 1) or (m == 1)):
	    if (n == 1):
	        ret_values.append((m // 2))
	    elif (m == 1):
	        ret_values.append((n // 2))
	elif (((m % 2) != 0) and ((n % 2) != 0)):
	    if (m > n):
	        e = m
	        r = n
	    else:
	        e = n
	        r = m
	    u = (e - 1)
	    b = ((u * r) // 2)
	    v = (r // 2)
	    ret_values.append((b + v))
	else:
	    fuck = ((m * n) // 2)
	    ret_values.append(fuck)

	return ret_values
