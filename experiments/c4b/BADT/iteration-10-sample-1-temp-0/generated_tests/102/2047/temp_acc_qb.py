def patched_func(*args):
	global_list = []
	
	(x, y, z) = map(int, args[0].split())
	if ((x + y) <= z):
	    global_list.append(((x * 2) + (y * 2)))
	elif (x == y == z):
	    global_list.append((x * 3))
	elif ((x > y) and (x > z)):
	    global_list.append(((y * 2) + (z * 2)))
	elif ((y > x) and (y > z)):
	    global_list.append(((x * 2) + (z * 2)))
	else:
	    global_list.append(((x + y) + z))
	return global_list