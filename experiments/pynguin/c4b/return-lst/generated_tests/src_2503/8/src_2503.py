def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	ret_values.append(('Impossible' if ((n == 0) and (m != 0)) else ('%d %d' % ((n + max(0, (m - n))), (n + max(0, (m - 1)))))))

	return ret_values
