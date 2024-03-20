def func(*args):
	
	inp = args[0].split()
	c = int(inp[0])
	v0 = int(inp[1])
	v1 = int(inp[2])
	a = int(inp[3])
	l = int(inp[4])
	nbpagerest = c
	day = 1
	while (nbpagerest >= 0):
	    if (day > 1):
	        nbpagerest = (nbpagerest + l)
	        if ((v0 + ((day - 1) * a)) <= v1):
	            nbpagerest = ((nbpagerest - v0) - ((day - 1) * a))
	        else:
	            nbpagerest = (nbpagerest - v1)
	    else:
	        nbpagerest = (nbpagerest - v0)
	    if (nbpagerest <= 0):
	        break
	    day = (day + 1)
	return(day)
