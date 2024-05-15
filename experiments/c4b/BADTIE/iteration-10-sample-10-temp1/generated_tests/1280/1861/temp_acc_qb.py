def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	m = [int(i) for i in args[1].split()]
	m.sort()
	m = m[::(- 1)]
	months = 0
	g = 0
	if (sum(m) < k):
	    global_list.append((- 1))
	else:
	    while (g < k):
	        g += m[months]
	        months += 1
	    global_list.append(months)
	return global_list