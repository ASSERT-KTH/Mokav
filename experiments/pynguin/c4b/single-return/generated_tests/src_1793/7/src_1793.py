def func(*args):
	
	p = int(args[0])
	x = 0
	x = ((p // 3) * 2)
	p = (p % 3)
	while p:
	    p = (p - 1)
	    x = (x + 1)
	    if (p <= 1):
	        break
	    p = (p - 2)
	    x = (x + 1)
	return(x)
