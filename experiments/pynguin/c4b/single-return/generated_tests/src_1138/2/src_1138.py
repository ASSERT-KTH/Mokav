def func(*args):
	
	from math import ceil
	n = int(args[0])
	if ((n & 1) == 0):
	    ans = (ceil((n / 4)) - 1)
	else:
	    ans = 0
	return(ans)
