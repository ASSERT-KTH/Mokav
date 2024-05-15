def original_func(*args):
	global_list = []
	
	
	def mult(x1, y1, x2, y2):
	    return ((x1 * y2) - (x2 * y1))
	(xa, ya) = [int(item) for item in args[0].split()]
	(xb, yb) = [int(item) for item in args[1].split()]
	(xc, yc) = [int(item) for item in args[2].split()]
	(x1, y1) = ((xa - xb), (ya - yb))
	(x2, y2) = ((xa - xc), (ya - yc))
	if (mult(x1, y1, x2, y2) > 0):
	    global_list.append('LEFT')
	elif (mult(x1, y1, x2, y2) < 0):
	    global_list.append('RIGHT')
	else:
	    global_list.append('TOWARD')
	return global_list