def func(*args):
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	d = int(args[3])
	n = ((((a * 8) + (b * 4)) + (c * 2)) + d)
	a = '0101000011011011'
	return(a[n])
