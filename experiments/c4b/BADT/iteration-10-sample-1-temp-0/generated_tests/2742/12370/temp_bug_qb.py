def original_func(*args):
	global_list = []
	
	a = int(args[0])
	x = (a % 2)
	if (x == 1):
	    b = int((a / 2))
	    b = (b - 1)
	    (global_list.append('7'),)
	    for i in range(0, b):
	        (global_list.append('1'),)
	else:
	    b = int((a / 2))
	    for i in range(0, b):
	        (global_list.append('1'),)
	return global_list