def func(*args):
	ret_values = []
	
	(k, b, n, t) = map(int, args[0].split())
	cur = 1
	dec = 1
	while (dec <= n):
	    cur = ((cur * k) + b)
	    if (cur > t):
	        break
	    dec += 1
	ret_values.append(((n - dec) + 1))

	return ret_values
