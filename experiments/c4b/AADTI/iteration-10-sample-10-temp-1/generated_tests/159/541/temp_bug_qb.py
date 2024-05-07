def original_func(*args):
	global_list = []
	
	s = args[0].split()
	x = int(s[0])
	if (s[2][0] == 'w'):
	    if (x >= 5):
	        global_list.append((52 + 1))
	    else:
	        global_list.append(52)
	elif (x <= 29):
	    global_list.append(12)
	elif (x == 30):
	    global_list.append(11)
	else:
	    global_list.append(7)
	return global_list