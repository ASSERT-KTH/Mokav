def func(*args):
	ret_values = []
	
	(l, r, k) = [int(i) for i in args[0].split()]
	i = 0
	g = True
	while True:
	    t = (k ** i)
	    if ((t <= r) and (t >= l)):
	        g = False
	        ret_values.append(t, end=' ')
	    elif (t > l):
	        break
	    i += 1
	if g:
	    ret_values.append((- 1))

	return ret_values
