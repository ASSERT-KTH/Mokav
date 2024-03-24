def func(*args):
	
	(a, b) = [int(x) for x in args[0].split()]
	mins = 0
	while ((a > 0) and (b > 0)):
	    if ((a == 1) and (b == 1)):
	        break
	    mins += 1
	    if (a < b):
	        a += 1
	        b -= 2
	    else:
	        a -= 2
	        b += 1
	return(mins)
