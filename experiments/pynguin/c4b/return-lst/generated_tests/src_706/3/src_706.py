def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	r = (max(n, m) - 1)
	g = (6 - r)
	if ((6 % g) == 0):
	    ret_values.append((('1' + '/') + str((6 // g))))
	elif ((g % 2) == 0):
	    ret_values.append(((str((g // 2)) + '/') + str('3')))
	else:
	    ret_values.append(((str(g) + '/') + '6'))

	return ret_values
