def func(*args):
	
	n = int(args[0])
	basic = (2 * (n // 7))
	maxwknds = int(basic)
	if ((n % 7) >= 2):
	    maxwknds += 2
	elif ((n % 7) > 0):
	    maxwknds += 1
	if ((n % 7) == 6):
	    basic += 1
	return(basic, maxwknds)
