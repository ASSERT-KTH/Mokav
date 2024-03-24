def func(*args):
	ret_values = []
	
	(t, s, x) = map(int, args[0].split())
	if (x < t):
	    exit(ret_values.append('NO'))
	ret_values.append(('YES' if ((x == t) or (((x - t) % s) == 0) or (((((x - t) - 1) % s) == 0) and ((x != (t + 1)) or (s == 1)))) else 'NO'))

	return ret_values
