def func(*args):
	ret_values = []
	
	from itertools import product
	(x, t, a, b, da, db) = map(int, args[0].split())
	ans = 0
	(la, lb) = ([0], [0])
	for i in range(t):
	    la += [(a - (i * da))]
	    lb += [(b - (i * db))]
	for sx in product(la, lb):
	    if ((sx[0] + sx[1]) == x):
	        ans = 1
	        break
	ret_values.append(['NO', 'YES'][ans])

	return ret_values
