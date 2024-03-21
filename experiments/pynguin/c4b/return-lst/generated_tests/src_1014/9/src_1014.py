def func(*args):
	ret_values = []
	
	n = int(args[0])
	l = args[1]
	l = [int(i) for i in l.split()]
	l = sorted(l)
	ret_values.append(l[(len(l) // 2)])

	return ret_values
