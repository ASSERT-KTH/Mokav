def patched_func(*args):
	global_list = []
	
	'input\n6 of month\n'
	s = args[0].split()
	(n, t) = (int(s[0]), s[2])
	d = (list(range(1, 30)) * 12)
	d += (([30] * 11) + ([31] * 7))
	if ((t == 'week') and ((n == 5) or (n == 6))):
	    global_list.append(53)
	elif (t == 'week'):
	    global_list.append(52)
	else:
	    global_list.append(d.count(n))
	return global_list