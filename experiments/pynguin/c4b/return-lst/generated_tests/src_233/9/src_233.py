def func(*args):
	ret_values = []
	
	k = int(args[0])
	x = sorted(list(map(int, args[1].split())))
	(c, s) = (0, 0)
	for i in range(11, (- 1), (- 1)):
	    if (s >= k):
	        break
	    s += x[i]
	    c += 1
	if (s >= k):
	    ret_values.append(c)
	else:
	    ret_values.append('-1')

	return ret_values
