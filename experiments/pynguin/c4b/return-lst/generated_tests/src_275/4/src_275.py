def func(*args):
	ret_values = []
	
	(n, m, z) = map(int, args[0].split())
	if (n > m):
	    a = n
	else:
	    a = m
	b = 0
	for i in range(a, 10001):
	    if (((a % n) == 0) and ((a % m) == 0)):
	        b = a
	        break
	    a = (a + 1)
	if (b == 0):
	    ret_values.append(0)
	else:
	    ret_values.append(int((z / b)))

	return ret_values
