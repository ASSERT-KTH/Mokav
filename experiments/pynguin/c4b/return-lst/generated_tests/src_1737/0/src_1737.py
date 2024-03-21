def func(*args):
	ret_values = []
	
	(q, w, e) = map(int, args[0].split())
	a = (w - q)
	if (q == w):
	    ret_values.append('YES')
	elif (e == 0):
	    ret_values.append('NO')
	elif ((a * e) >= 0):
	    if ((a % e) == 0):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
