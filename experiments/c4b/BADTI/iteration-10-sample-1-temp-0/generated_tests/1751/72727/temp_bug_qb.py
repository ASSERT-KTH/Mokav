def original_func(*args):
	global_list = []
	
	(xa, ya) = [float(s) for s in args[0].split()]
	(xb, yb) = [float(s) for s in args[1].split()]
	(xc, yc) = [float(s) for s in args[2].split()]
	falcon = ((((xb - xa) * (yc - yb)) * (xc - xb)) * (yb - ya))
	if (falcon == 0):
	    global_list.append('RIGHT')
	elif (falcon < 0):
	    global_list.append('LEFT')
	else:
	    global_list.append('TOWARDS')
	return global_list