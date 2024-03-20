def func(*args):
	
	n = int(args[0])
	d = int((n / 7))
	r = (n % 7)
	vmin = (2 * d)
	vmax = ((2 * d) + min(2, r))
	if (r == 6):
	    vmin = (vmin + 1)
	return(vmin, vmax)
