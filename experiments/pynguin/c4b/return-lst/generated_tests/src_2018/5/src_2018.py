def func(*args):
	ret_values = []
	
	(n, m, k) = (int(i) for i in args[0].split())
	k -= 1
	row = (int((k / (2 * m))) + 1)
	col = (int(((k % (2 * m)) / 2)) + 1)
	place = ('R' if ((k % 2) == 1) else 'L')
	ret_values.append(row, col, place)

	return ret_values
