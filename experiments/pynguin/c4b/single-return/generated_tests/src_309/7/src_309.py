def func(*args):
	
	if (__name__ == '__main__'):
	    refer = ((1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1), (0, 2, 1), (0, 1, 2))
	    n = int(args[0])
	    x = int(args[1])
	    return(refer[((n % 6) - 1)][x])
