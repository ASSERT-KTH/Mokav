def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	if ((k == 1) or (l == 1) or (m == 1) or (n == 1)):
	    ret_values.append(d)
	else:
	    a = [int(x) for x in range(k, (d + 1), k)]
	    b = [int(x) for x in range(l, (d + 1), l)]
	    c = [int(x) for x in range(m, (d + 1), m)]
	    d = [int(x) for x in range(n, (d + 1), n)]
	    ret_values.append(len(set((((a + b) + c) + d))))

	return ret_values
