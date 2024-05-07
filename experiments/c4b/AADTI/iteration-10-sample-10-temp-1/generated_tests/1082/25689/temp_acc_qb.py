def patched_func(*args):
	global_list = []
	
	from math import log
	n = int(args[0])
	m = int(args[1])
	imp = (- 1)
	i = 0
	while ((m >= n) and ((m % n) == 0)):
	    m /= n
	    i += 1
	if (m == 1):
	    imp = i
	if (imp != (- 1)):
	    global_list.append('YES')
	    global_list.append((int(imp) - 1))
	else:
	    global_list.append('NO')
	return global_list