def original_func(*args):
	global_list = []
	
	n = int(args[0])
	for i in range((n + 1), 1000):
	    if (len({int(j) for j in ' '.join(str(i)).split()}) == 4):
	        global_list.append(i)
	        break
	return global_list