def func(*args):
	ret_values = []
	
	(c, v0, v1, a, l) = (int(i) for i in args[0].split())
	d = 1
	sum = v0
	v = 0
	while (sum < c):
	    v = min((v0 + (a * d)), v1)
	    sum = ((sum + v) - l)
	    d = (d + 1)
	ret_values.append(d)

	return ret_values
