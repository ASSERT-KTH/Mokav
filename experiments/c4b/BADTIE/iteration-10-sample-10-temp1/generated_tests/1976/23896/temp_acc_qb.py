def patched_func(*args):
	global_list = []
	
	num = int(args[0])
	stones = list(args[1])
	l = []
	first = stones[0]
	n = 0
	for i in range(1, len(stones)):
	    if (first == stones[i]):
	        l.append(stones[i])
	    else:
	        first = stones[i]
	global_list.append(len(l))
	return global_list