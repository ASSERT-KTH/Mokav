def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	y = 5
	z = 1
	while (x > (y * z)):
	    x -= (y * z)
	    z *= 2
	if ((x - (z * 1)) < 1):
	    global_list.append('Sheldon')
	elif ((x - (z * 2)) < 1):
	    global_list.append('Leonard')
	elif ((x - (z * 3)) < 1):
	    global_list.append('Penny')
	elif ((x - (z * 4)) < 1):
	    global_list.append('Rajesh')
	elif ((x - (z * 5)) < 1):
	    global_list.append('Howard')
	return global_list