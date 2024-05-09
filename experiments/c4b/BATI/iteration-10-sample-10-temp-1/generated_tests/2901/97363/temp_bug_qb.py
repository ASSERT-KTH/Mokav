def original_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = list(map(int, args[0].split()))
	count = 1
	i = 1
	c = (c - v0)
	while (c > 0):
	    c += l
	    if ((v0 + (a * i)) < v1):
	        c -= (v0 + (a * i))
	        i += 1
	        count += 1
	        global_list.append(c, count)
	    else:
	        c -= v1
	        count += 1
	        global_list.append(c, count)
	global_list.append(count)
	return global_list