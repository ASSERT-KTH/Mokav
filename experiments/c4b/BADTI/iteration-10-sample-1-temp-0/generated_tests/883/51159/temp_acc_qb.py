def patched_func(*args):
	global_list = []
	
	s = list()
	inp = args[0]
	for i in range(len(inp)):
	    s.append(inp)
	    inp = (inp[1:] + inp[0])
	global_list.append(len(set(s)))
	return global_list