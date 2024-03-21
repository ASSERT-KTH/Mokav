def func(*args):
	ret_values = []
	
	n = int(args[0])
	x = 1234567
	y = 123456
	z = 1234
	for i in range(0, n):
	    if ((i * x) > n):
	        break
	    m = (n - (x * i))
	    for j in range(0, n):
	        if ((j * y) > m):
	            break
	        l = (m - (y * j))
	        if ((l % 1234) == 0):
	            ret_values.append('YES')
	            exit(0)
	ret_values.append('NO')

	return ret_values
