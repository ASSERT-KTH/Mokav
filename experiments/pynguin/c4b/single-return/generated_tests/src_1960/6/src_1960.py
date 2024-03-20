def func(*args):
	
	n = int(args[0])
	get = []
	x = 1
	out = ''
	for i in range(1, n):
	    x = (x + i)
	    if (x > n):
	        x = (x % n)
	    if (i == (n - 1)):
	        out += str(x)
	    else:
	        out += (str(x) + ' ')
	return(out)
