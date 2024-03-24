def func(*args):
	ret_values = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	t = v0
	k = 1
	while (t < c):
	    v0 = (v0 + a)
	    if (v0 > v1):
	        v0 = v1
	    t = ((t - l) + v0)
	    k += 1
	ret_values.append(k)

	return ret_values
