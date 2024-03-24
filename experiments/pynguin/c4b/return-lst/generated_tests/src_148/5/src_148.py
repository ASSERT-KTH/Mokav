def func(*args):
	ret_values = []
	
	'input\n4 3 9\n'
	(n, m, k) = map(int, args[0].split())
	if ((k % (2 * m)) == 0):
	    l = (k // (2 * m))
	else:
	    l = ((k // (2 * m)) + 1)
	ret_values.append(l, end=' ')
	if ((((k + 1) // 2) % m) == 0):
	    ret_values.append(m, end=' ')
	else:
	    ret_values.append((((k + 1) // 2) % m), end=' ')
	ret_values.append(('L' if ((k % 2) == 1) else 'R'))

	return ret_values
