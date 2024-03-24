def func(*args):
	
	n = int(args[0])
	res = int((n / 3))
	res *= 2
	if ((n % 3) > 0):
	    res += 1
	return(res)
