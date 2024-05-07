def original_func(*args):
	global_list = []
	
	num = int(args[0])
	stones = args[1]
	l = []
	first = stones[0]
	n = 0
	for i in range(1, num):
	    if (first == stones[i]):
	        n += 1
	    else:
	        first = stones[i]
	        l.append(n)
	        n = 0
	if len(l):
	    global_list.append(max(l))
	else:
	    global_list.append(n)
	return global_list