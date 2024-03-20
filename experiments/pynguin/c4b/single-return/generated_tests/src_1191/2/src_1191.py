def func(*args):
	
	import sys
	n = int(args[0])
	min = ((n // 7) * 2)
	k = (n % 7)
	if (k > 4):
	    min += (k - 5)
	max = (n % 7)
	if (max > 2):
	    max = 2
	return(min, (((n // 7) * 2) + max))
