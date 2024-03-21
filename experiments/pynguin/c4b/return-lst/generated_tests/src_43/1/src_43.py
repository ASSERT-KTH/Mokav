def func(*args):
	ret_values = []
	
	import sys
	size = int(sys.stdin.readline().strip())
	if (size == 2):
	    ret_values.append('NO')
	    sys.exit(0)
	ret_values.append(('YES' if ((size % 2) == 0) else 'NO'))

	return ret_values
