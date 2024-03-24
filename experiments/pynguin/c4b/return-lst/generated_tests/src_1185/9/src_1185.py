def func(*args):
	ret_values = []
	
	(l, r) = list(map(int, args[0].split()))
	if ((l == r) and (l == 0)):
	    ret_values.append('NO')
	else:
	    ret_values.append(('YES' if (abs((l - r)) <= 1) else 'NO'))

	return ret_values
