def original_func(*args):
	global_list = []
	
	n = int(args[0])
	(kid, count, res) = (1, 1, [])
	for i in range((n - 1)):
	    kid = ((kid + count) % n)
	    res.append(kid)
	    count += 1
	global_list.append(*res)
	return global_list