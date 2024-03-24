def func(*args):
	ret_values = []
	
	n = int(args[0])
	R = (lambda : map(int, args[1].split()))
	l = list(R())
	l.sort()
	ret_values.append(l[((n - 1) // 2)])

	return ret_values
