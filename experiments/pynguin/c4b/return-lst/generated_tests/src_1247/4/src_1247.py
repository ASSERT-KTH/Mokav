def func(*args):
	ret_values = []
	
	(n, a) = map(int, args[0].split())
	alp = ((180 * (n - 2)) / n)
	minR = 181
	x = 3
	angle = 0
	for i in range(3, (n + 1)):
	    angle = (((180 * (i - 2)) - (alp * (i - 2))) / 2)
	    if (abs((angle - a)) < minR):
	        minR = abs((angle - a))
	        x = i
	ret_values.append('2 1', x)

	return ret_values
