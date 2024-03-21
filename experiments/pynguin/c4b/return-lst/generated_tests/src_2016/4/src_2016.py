def func(*args):
	ret_values = []
	
	(n, m, k) = map(int, args[0].split())
	p = ((k - 1) // 2)
	y = ((p // m) + 1)
	x = ((p % m) + 1)
	if ((k % 2) == 0):
	    ret_values.append(y, x, 'R')
	if ((k % 2) == 1):
	    ret_values.append(y, x, 'L')

	return ret_values
