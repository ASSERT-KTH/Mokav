def original_func(*args):
	global_list = []
	
	'input\n581\n196122941\n'
	from math import log
	(k, l) = (int(args[0]), int(args[1]))
	if (log(l, k) == float(log(l, k))):
	    global_list.append('YES')
	    global_list.append(int((log(l, k) - 1)))
	else:
	    global_list.append('NO')
	return global_list