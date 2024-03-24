def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split(' '))
	c = ((n * (n + 1)) // 2)
	m %= c
	for i in range(1, (n + 1)):
	    if (((i * (i + 1)) // 2) > m):
	        m -= ((i * (i - 1)) // 2)
	        ret_values.append(m)
	        break

	return ret_values
