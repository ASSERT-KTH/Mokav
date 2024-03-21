def func(*args):
	ret_values = []
	
	l = [int(i) for i in args[0].split()]
	l.sort()
	ret_values.append(((l[1] - l[0]) + (l[2] - l[1])))

	return ret_values
