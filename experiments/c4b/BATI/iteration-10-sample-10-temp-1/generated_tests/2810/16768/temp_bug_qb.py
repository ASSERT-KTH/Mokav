def original_func(*args):
	global_list = []
	
	n = int(args[0])
	cost = 0
	for i in range(1, (n + 1)):
	    for j in range((i + 1), (n + 1)):
	        cost += ((i + j) % (n + 1))
	global_list.append(cost)
	return global_list