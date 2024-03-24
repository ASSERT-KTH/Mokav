def func(*args):
	ret_values = []
	
	(t, s, k) = map(int, args[0].split())
	if ((k < t) or ((k - t) == 1)):
	    ret_values.append('NO')
	elif (k == t):
	    ret_values.append('YES')
	else:
	    k -= t
	    ret_values.append(('YES' if (((k % s) == 0) or ((k % s) == 1)) else 'NO'))

	return ret_values
