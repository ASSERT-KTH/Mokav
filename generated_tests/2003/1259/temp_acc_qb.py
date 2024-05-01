def patched_func(*args):
	global_list = []
	
	y = int(args[0])
	y1 = ['0', '0', '0', '0']
	y = (y + 1)
	while (y <= 100000):
	    y1[0] = int((y / 1000))
	    y1[1] = int((int((y / 100)) % 10))
	    y1[2] = int((int((y / 10)) % 10))
	    y1[3] = int((y % 10))
	    if ((y1[0] != y1[1]) and (y1[0] != y1[2]) and (y1[0] != y1[3]) and (y1[1] != y1[2]) and (y1[1] != y1[3]) and (y1[2] != y1[3])):
	        global_list.append(y)
	        break
	    else:
	        y = (y + 1)
	return global_list