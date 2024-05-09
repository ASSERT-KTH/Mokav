def patched_func(*args):
	global_list = []
	
	u = int(args[0])
	if (u == 1):
	    global_list.append(1)
	if (2 <= u <= 5):
	    if (u == 3):
	        global_list.append(5)
	    else:
	        global_list.append(3)
	if (6 <= u <= 13):
	    global_list.append(5)
	if (14 <= u <= 25):
	    global_list.append(7)
	if (26 <= u <= 41):
	    global_list.append(9)
	if (42 <= u <= 61):
	    global_list.append(11)
	if (62 <= u <= 85):
	    global_list.append(13)
	if (86 <= u <= 100):
	    global_list.append(15)
	return global_list