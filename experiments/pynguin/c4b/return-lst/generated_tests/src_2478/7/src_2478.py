def func(*args):
	ret_values = []
	
	(xa, ya) = [int(s) for s in args[0].split()]
	(xb, yb) = [int(s) for s in args[1].split()]
	(xc, yc) = [int(s) for s in args[2].split()]
	falcon = (((xb - xa) * (yc - yb)) - ((xc - xb) * (yb - ya)))
	if (falcon > 0):
	    ret_values.append('LEFT')
	elif (falcon < 0):
	    ret_values.append('RIGHT')
	else:
	    ret_values.append('TOWARDS')

	return ret_values
