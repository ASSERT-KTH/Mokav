def patched_func(*args):
	global_list = []
	
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
	            global_list.append('YES')
	            exit(0)
	global_list.append('NO')
	return global_list