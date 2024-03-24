def func(*args):
	ret_values = []
	
	import sys
	(a, b) = map(int, sys.stdin.readline().split())
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	    exit()
	t = abs((a - b))
	if ((t == 0) or (t == 1)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
