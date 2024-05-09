def patched_func(*args):
	global_list = []
	
	(xa, ya) = [int(s) for s in args[0].split()]
	(xb, yb) = [int(s) for s in args[1].split()]
	(xc, yc) = [int(s) for s in args[2].split()]
	falcon = (((xb - xa) * (yc - yb)) - ((xc - xb) * (yb - ya)))
	if (falcon > 0):
	    global_list.append('LEFT')
	elif (falcon < 0):
	    global_list.append('RIGHT')
	else:
	    global_list.append('TOWARDS')
	return global_list