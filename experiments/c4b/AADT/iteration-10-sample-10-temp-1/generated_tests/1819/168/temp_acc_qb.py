def patched_func(*args):
	global_list = []
	
	(y, k, n) = [int(i) for i in args[0].split()]
	a = (y % k)
	m = []
	for i in range(n):
	    h = ((i * k) - a)
	    num = (h + y)
	    if (num <= n):
	        if (h > 0):
	            m.append(h)
	    else:
	        break
	if (len(m) > 0):
	    global_list.append(*m)
	else:
	    global_list.append((- 1))
	return global_list