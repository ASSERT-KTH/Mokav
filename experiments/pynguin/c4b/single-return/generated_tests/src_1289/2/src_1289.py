def func(*args):
	
	(k, b, n, t) = map(int, args[0].split())
	cur = 1
	dec = 1
	while (dec <= n):
	    cur = ((cur * k) + b)
	    if (cur > t):
	        break
	    dec += 1
	return(((n - dec) + 1))
