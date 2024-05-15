def original_func(*args):
	global_list = []
	
	y = int(args[0])
	l = len(str(y))
	k = 0
	t = (- 1)
	count = 0
	while ((k < l) and (t == (- 1))):
	    h = (y % 10)
	    if ((h == 7) or (h == 4)):
	        t = (- 1)
	    else:
	        t = 1
	    y //= 10
	    k += 1
	if (k == l):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list