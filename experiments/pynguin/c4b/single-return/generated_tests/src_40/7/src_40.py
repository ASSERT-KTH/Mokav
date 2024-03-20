def func(*args):
	
	line = sorted([int(x) for x in args[0].split(' ')])
	return(str((line[2] - line[0])))
