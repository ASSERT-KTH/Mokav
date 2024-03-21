def func(*args):
	ret_values = []
	
	import sys
	(start, value, increment) = map(int, sys.stdin.readline().strip().split())
	if (start == value):
	    ret_values.append('YES')
	    exit()
	if ((value > start) and (increment > 0) and ((value % increment) == (start % increment))):
	    ret_values.append('YES')
	    exit()
	if ((value < start) and (increment < 0) and ((value % increment) == (start % increment))):
	    ret_values.append('YES')
	    exit()
	ret_values.append('NO')

	return ret_values
