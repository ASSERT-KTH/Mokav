def original_func(*args):
	global_list = []
	
	l = [1, 2, 3, 4, 5, 6]
	(a, b) = args[0].strip().split(' ')
	(a, b) = (int(a), int(b))
	if (a == b):
	    global_list.append('1/1')
	elif ((a == 6) or (b == 6)):
	    global_list.append('0/1')
	else:
	    c = (7 - max(a, b))
	    if (c == 1):
	        global_list.append('1/6')
	    elif (c == 2):
	        global_list.append('1/3')
	    elif (c == 3):
	        global_list.append('1/2')
	    elif (c == 4):
	        global_list.append('2/3')
	return global_list