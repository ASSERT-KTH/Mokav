def func(*args):
	
	(n, m) = map(int, args[0].split())
	x = args[1]
	while m:
	    x = x.replace('BG', 'GB')
	    m -= 1
	return(x)
