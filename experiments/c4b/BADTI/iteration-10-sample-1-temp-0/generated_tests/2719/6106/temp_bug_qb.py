def original_func(*args):
	global_list = []
	
	s = args[0]
	l = list(s)
	L_w = int(l[0])
	B_w = int(l[2])
	i = 0
	while (L_w <= B_w):
	    L_w *= 3
	    B_w *= 2
	    i += 1
	else:
	    global_list.append(i)
	return global_list