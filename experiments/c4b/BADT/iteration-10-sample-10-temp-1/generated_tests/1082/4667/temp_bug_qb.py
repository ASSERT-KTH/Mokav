def original_func(*args):
	global_list = []
	
	from math import log
	a = int(args[0])
	b = int(args[1])
	s = False
	n = 0
	for i in range(1, (int(log(b, a)) + 1)):
	    if ((a ** i) == b):
	        s = True
	        n = (i - 1)
	if s:
	    global_list.append('YES\n{}'.format(n))
	else:
	    global_list.append('NO')
	return global_list