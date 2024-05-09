def original_func(*args):
	global_list = []
	
	(last, res) = ((- 1), 0)
	s = args[0]
	for (i, c) in enumerate(s):
	    if (c in 'AEIOUY'):
	        res = max(res, (i - last))
	        last = i
	res = max(res, (len(s) - i))
	global_list.append(res)
	return global_list