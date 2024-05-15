def original_func(*args):
	global_list = []
	
	l1 = args[0]
	l2 = args[1]
	l3 = args[2]
	l4 = args[3]
	l5 = args[4]
	l6 = args[5]
	l7 = args[6]
	l8 = args[7]
	c = 0
	if (l1.count('B') == 8):
	    c += 1
	else:
	    c += l1.count('B')
	if (l2.count('B') == 8):
	    c += 1
	else:
	    c += l2.count('B')
	if (l3.count('B') == 8):
	    c += 1
	else:
	    c += l3.count('B')
	if (l4.count('B') == 8):
	    c += 1
	else:
	    c += l4.count('B')
	if (l5.count('B') == 8):
	    c += 1
	else:
	    c += l5.count('B')
	if (l6.count('B') == 8):
	    c += 1
	else:
	    c += l7.count('B')
	if (l7.count('B') == 8):
	    c += 1
	else:
	    c += l7.count('B')
	if (l8.count('B') == 8):
	    c += 1
	else:
	    c += l8.count('B')
	global_list.append(c)
	return global_list