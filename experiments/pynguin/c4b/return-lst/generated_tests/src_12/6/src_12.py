def func(*args):
	ret_values = []
	
	from math import *
	(n, R, r) = map(int, args[0].split())
	if (n < 3):
	    exit(ret_values.append(['NO', 'YES'][((n * r) <= (R + 1e-09))]))
	theta = (((pi / 180) * 360) / n)
	theta2 = ((180 - (360 / n)) / 2)
	a = ((2 * r) + ((2 * r) * cos(((pi / 180) * theta2))))
	b = ((a * sin(((pi - theta) / 2))) / sin(theta))
	ret_values.append(['NO', 'YES'][(b <= (R + 1e-09))])

	return ret_values
