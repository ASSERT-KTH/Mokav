def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = list(map(int, args[1].split(' ')))
	a.sort()
	cnt = 0
	x = 12
	while ((n > 0) and (x > 0)):
	    n -= a[(x - 1)]
	    x -= 1
	    cnt += 1
	if ((x >= 0) and (n <= 0)):
	    ret_values.append(cnt)
	else:
	    ret_values.append((- 1))

	return ret_values
