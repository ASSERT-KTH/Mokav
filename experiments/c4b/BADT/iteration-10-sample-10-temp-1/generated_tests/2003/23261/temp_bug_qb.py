def original_func(*args):
	global_list = []
	
	n = args[0]
	for i in range((int(n) + 1), 9001):
	    tmp = str(i)
	    if ((tmp[0] != tmp[1]) and (tmp[0] != tmp[2]) and (tmp[0] != tmp[3]) and (tmp[1] != tmp[2]) and (tmp[1] != tmp[3]) and (tmp[2] != tmp[3])):
	        global_list.append(tmp)
	        break
	return global_list