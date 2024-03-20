def func(*args):
	
	a = int(args[0])
	b = []
	b = list(args[1])
	c = 0
	j = 0
	while (c < (len(b) - 1)):
	    if (b[c] == b[(c + 1)]):
	        j = (j + 1)
	    c = (c + 1)
	return(j)
