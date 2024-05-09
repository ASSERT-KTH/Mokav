def patched_func(*args):
	global_list = []
	
	s = args[0].split()
	s1 = int(s[0])
	if (s[2] == 'week'):
	    if ((s1 == 5) or (s1 == 6)):
	        global_list.append(53)
	    else:
	        global_list.append(52)
	elif (s1 == 31):
	    global_list.append(7)
	elif (s1 == 30):
	    global_list.append(11)
	else:
	    global_list.append(12)
	return global_list