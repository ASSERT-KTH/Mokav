def func(*args):
	ret_values = []
	
	import sys
	n = int(args[0])
	for i in range(1, (n + 1), 1):
	    if (((i * (i + 1)) / 2) == n):
	        ret_values.append('YES')
	        sys.exit()
	ret_values.append('NO')
	sys.exit()

	return ret_values
