def func(*args):
	ret_values = []
	
	n = int(args[0])
	k = args[1].split(' ')
	l = []
	for _ in k:
	    l.append(int(_))
	l = sorted(l)
	ret_values.append(l[int((len(l) / 2))])

	return ret_values
