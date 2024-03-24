def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	dividers = [k, l, m, n]
	siev = range(1, (d + 1))
	S = 0
	for i in siev:
	    for j in dividers:
	        if ((i % j) == 0):
	            S += 1
	            break
	ret_values.append(S)

	return ret_values
