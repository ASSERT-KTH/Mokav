def original_func(*args):
	global_list = []
	
	k = int(args[0])
	x = sorted(list(map(int, args[1].split())))
	(c, s) = (0, 0)
	for i in range(11, (- 1), (- 1)):
	    if (s >= k):
	        break
	    s += x[i]
	    c += 1
	global_list.append(c)
	return global_list