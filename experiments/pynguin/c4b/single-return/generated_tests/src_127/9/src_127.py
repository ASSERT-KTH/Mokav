def func(*args):
	
	(r, b) = map(int, args[0].split())
	can = 0
	cant = 0
	if (r > b):
	    while (b > 0):
	        b -= 1
	        r -= 1
	        can += 1
	    while (r > 1):
	        r -= 2
	        cant += 1
	elif (r < b):
	    while (r > 0):
	        r -= 1
	        b -= 1
	        can += 1
	    while (b > 1):
	        b -= 2
	        cant += 1
	else:
	    while (r > 0):
	        r -= 1
	        can += 1
	return(can, cant)
