def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	g = (lambda x, y: (g((y % x), x) if x else y))
	c = ((a // g(a, b)) * b)
	A = a
	B = b
	r = t = 0
	while 1:
	    if (A < B):
	        r += (A - t)
	        t = A
	        A += a
	    elif (B < A):
	        r += (t - B)
	        t = B
	        B += b
	    else:
	        r += ((A - t) * (0 if (a == b) else [(- 1), 1][(a > b)]))
	        break
	ret_values.append(('Masha' if (r < 0) else ['Equal', 'Dasha'][(r > 0)]))

	return ret_values
