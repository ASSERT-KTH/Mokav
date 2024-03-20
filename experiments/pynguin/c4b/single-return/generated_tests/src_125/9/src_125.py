def func(*args):
	
	n = args[0]
	x = n.split()[0]
	y = n.split()[1]
	z = n.split()[2]
	t = [((int(x) + int(y)) + int(z)), ((2 * int(x)) + (2 * int(y))), ((2 * int(y)) + (2 * int(z))), ((2 * int(x)) + (2 * int(z)))]
	return(min(t))
