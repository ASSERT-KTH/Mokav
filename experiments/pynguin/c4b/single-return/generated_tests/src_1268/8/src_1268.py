def func(*args):
	
	(d1, d2, d3) = args[0].split()
	d1 = int(d1)
	d2 = int(d2)
	d3 = int(d3)
	z = ((d1 + d2) + d3)
	if (z > ((2 * d1) + (2 * d3))):
	    z = ((2 * d1) + (2 * d3))
	elif (z > ((2 * d2) + (2 * d3))):
	    z = ((2 * d2) + (2 * d3))
	elif (z > ((2 * d1) + (2 * d2))):
	    z = ((2 * d1) + (2 * d2))
	return(z)
