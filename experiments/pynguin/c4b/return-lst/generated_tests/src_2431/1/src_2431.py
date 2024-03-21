def func(*args):
	ret_values = []
	
	a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
	(n, m) = map(int, args[0].split())
	if ((a[(- 1)] != n) and (a[(a.index(n) + 1)] == m)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
