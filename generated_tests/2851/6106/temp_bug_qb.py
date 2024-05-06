def original_func(*args):
	global_list = []
	
	s = args[0]
	l = s.split()
	v1 = int(l[0])
	v2 = int(l[1])
	i = 1
	while ((v1 > 0) and (v2 > 0)):
	    if ((i % 2) == 1):
	        v1 -= i
	    if ((i % 2) == 0):
	        v2 -= i
	    i += 1
	if (v1 < 0):
	    global_list.append('Vladik')
	else:
	    global_list.append('Valera')
	return global_list