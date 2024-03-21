def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = sorted(list(map(int, args[1].split())), key=int)
	(s, i) = (0, 0)
	while ((s < k) and (i > (- 12))):
	    i -= 1
	    s += a[i]
	if (s >= k):
	    ret_values.append((- i))
	else:
	    ret_values.append('-1')

	return ret_values
