def func(*args):
	
	n = int(args[0].strip())
	maxx = ((n // 7) * 2)
	minn = ((n // 7) * 2)
	if ((n % 7) > 1):
	    maxx += 2
	    if ((n % 7) == 6):
	        minn += 1
	else:
	    maxx += (n % 7)
	return(minn, maxx)
