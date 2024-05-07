def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split(' '))
	for i in range(1, 10001):
	    if ((((c - (a * i)) % b) == 0) and ((c - (a * i)) >= 0)):
	        global_list.append('Yes')
	        break
	else:
	    global_list.append('No')
	return global_list