def func(*args):
	ret_values = []
	
	'input\n0\n0 0 0 0 0 0 0 1 1 2 3 0\n'
	k = int(args[0])
	a = list(map(int, args[1].split()))
	if (sum(a) < k):
	    ret_values.append((- 1))
	elif (k == 0):
	    ret_values.append(0)
	else:
	    (s, t) = (0, 0)
	    a = sorted(a)[::(- 1)]
	    while (s < k):
	        s += a[0]
	        t += 1
	        del a[0]
	    ret_values.append(t)

	return ret_values
