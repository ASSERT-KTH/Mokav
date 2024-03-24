def func(*args):
	
	(a1, a2) = [int(x) for x in args[0].split(' ')]
	mins = 0
	while ((a1 > 0) and (a2 > 0)):
	    if ((a1 == 1) and (a2 == 1)):
	        break
	    mins += 1
	    if (a1 == min(a1, a2)):
	        a1 += 1
	        a2 -= 2
	    else:
	        a2 += 1
	        a1 -= 2
	return(mins)
