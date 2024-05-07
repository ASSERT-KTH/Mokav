def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = list(map(int, args[1].split(' ')))
	a.sort()
	cnt = 0
	x = 12
	while ((n > 0) and (x > 0)):
	    n -= a[(x - 1)]
	    x -= 1
	    cnt += 1
	if ((x >= 0) and (n < 0)):
	    global_list.append(cnt)
	else:
	    global_list.append((- 1))
	return global_list