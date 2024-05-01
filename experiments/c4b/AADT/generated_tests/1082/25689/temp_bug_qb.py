def original_func(*args):
	global_list = []
	
	from math import log
	n = int(args[0])
	m = int(args[1])
	imp = (log(m) / log(n))
	if (imp == int(imp)):
	    global_list.append('YES')
	    global_list.append((int(imp) - 1))
	else:
	    global_list.append('NO')
	return global_list