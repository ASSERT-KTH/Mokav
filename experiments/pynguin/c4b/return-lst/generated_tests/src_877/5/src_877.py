def func(*args):
	ret_values = []
	
	(x, y) = list(map(int, args[0].split()))
	a = True
	d = 1
	while a:
	    n = (x * 3)
	    m = (y * 2)
	    if (n > m):
	        ret_values.append(d)
	        a = False
	    elif (m >= n):
	        d += 1
	        x = n
	        y = m

	return ret_values
