def original_func(*args):
	global_list = []
	
	s = '123456789'
	for i in range(10, 20):
	    s += str(i)
	for i in range(100, 200):
	    s += str(i)
	for i in range(1000, 2000):
	    if (len(s) > 1000):
	        break
	    s += str(i)
	n = int(args[0])
	global_list.append(s[(n - 1)])
	return global_list