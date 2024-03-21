def func(*args):
	ret_values = []
	
	(x, t, a, b, c, d) = map(int, args[0].split())
	R = range(t)
	y = (x == 0)
	for i in R:
	    if ((x == (a - (c * i))) or (x == (b - (d * i)))):
	        y = 1
	    for j in R:
	        y |= (x == (((a + b) - (c * i)) - (d * j)))
	ret_values.append(['NO', 'YES'][y])

	return ret_values
