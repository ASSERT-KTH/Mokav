def func(*args):
	ret_values = []
	
	(t, s, x) = list(map(int, args[0].split()))
	if (t == x):
	    ret_values.append('YES')
	    exit()
	if (x < (s + t)):
	    ret_values.append('NO')
	    exit()
	if ((((x - t) % s) == 0) or ((((x - t) - 1) % s) == 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
