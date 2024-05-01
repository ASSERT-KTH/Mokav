def original_func(*args):
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
	if (26 <= u <= 40):
	    global_list.append(9)
	if (41 <= u <= 60):
	    global_list.append(11)
	if (61 <= u <= 84):
	    global_list.append(13)
	if (85 <= u <= 100):
	    global_list.append(15)
	return global_list