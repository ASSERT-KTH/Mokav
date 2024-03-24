def func(*args):
	
	import sys
	import math
	(r, g, b) = [int(x) for x in sys.stdin.readline().split()]
	res1 = 30
	res2 = 30
	res3 = 30
	i = 0
	if (r >= 2):
	    r -= 2
	    res1 += 0
	elif (r == 1):
	    r = 0
	    res1 += 0
	if (g >= 2):
	    g -= 2
	    res2 += 1
	elif (g == 1):
	    g = 0
	    res2 += 1
	if (b >= 2):
	    b -= 2
	    res3 += 2
	elif (b == 1):
	    b = 0
	    res3 += 2
	res1 += (int((r / 2)) * 3)
	if ((r % 2) != 0):
	    res1 += 3
	res2 += (int((g / 2)) * 3)
	if ((g % 2) != 0):
	    res2 += 3
	res3 += (int((b / 2)) * 3)
	if ((b % 2) != 0):
	    res3 += 3
	return(max([res1, res2, res3]))
