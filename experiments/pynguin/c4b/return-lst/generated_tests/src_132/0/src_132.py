def func(*args):
	ret_values = []
	
	'input\n1 1000000\n'
	(a, b) = map(int, args[0].split())
	s = 0
	n = str(list(range(a, (b + 1))))
	d = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
	for x in range(10):
	    s += (d[x] * n.count(str(x)))
	ret_values.append(s)

	return ret_values
