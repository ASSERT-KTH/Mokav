def func(*args):
	
	ins = list(map(int, args[0].split()))
	d1 = ins[0]
	d2 = ins[1]
	d3 = ins[2]
	mins = ((2 * d1) + (2 * d2))
	if (mins > ((d1 + d2) + d3)):
	    mins = ((d1 + d2) + d3)
	if (mins > ((2 * d1) + (2 * d3))):
	    mins = ((2 * d1) + (2 * d3))
	if (mins > ((2 * d2) + (2 * d3))):
	    mins = ((2 * d2) + (2 * d3))
	return(mins)
