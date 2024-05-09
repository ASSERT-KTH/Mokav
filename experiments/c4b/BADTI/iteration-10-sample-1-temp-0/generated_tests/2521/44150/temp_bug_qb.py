def original_func(*args):
	global_list = []
	
	n = args[0]
	ans = (2 ** (len(n) - 1))
	n1 = ''
	for i in range(1, len(n)):
	    if (int(n[i]) > 0):
	        n1 += '1'
	    else:
	        n1 += '0'
	n1 = (0 + int(n1))
	global_list.append((ans + n1))
	return global_list