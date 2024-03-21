def func(*args):
	ret_values = []
	
	'input\n6 of month\n'
	s = args[0].split()
	(n, t) = (int(s[0]), s[2])
	d = (list(range(1, 30)) * 12)
	d += (([30] * 11) + ([31] * 7))
	if ((t == 'week') and ((n == 5) or (n == 6))):
	    ret_values.append(53)
	elif (t == 'week'):
	    ret_values.append(52)
	else:
	    ret_values.append(d.count(n))

	return ret_values
