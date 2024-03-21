def func(*args):
	ret_values = []
	
	tl = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
	(n, m) = map(int, args[0].split())
	ans = (tl[(tl.index(n) + 1)] == m)
	ret_values.append(['NO', 'YES'][ans])

	return ret_values
