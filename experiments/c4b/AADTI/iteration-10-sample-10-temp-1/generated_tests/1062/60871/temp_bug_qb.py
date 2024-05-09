def original_func(*args):
	global_list = []
	
	a = args[0]
	c = a[0]
	q = len(a)
	f = []
	n = 0
	while (n < q):
	    e = ord(a[n])
	    if ((e == 52) or (e == 55)):
	        f.append(e)
	    else:
	        break
	    n = (n + 1)
	g = len(f)
	if ((g == q) and (q > 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list