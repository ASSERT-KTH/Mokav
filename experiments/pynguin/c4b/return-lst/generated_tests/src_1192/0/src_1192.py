def func(*args):
	ret_values = []
	
	import sys
	(a, b, c) = map(int, sys.stdin.readline().split())
	if (a == b):
	    ret_values.append('YES')
	elif (c == 0):
	    ret_values.append('NO')
	elif (((b - a) % c) == 0):
	    if (((b <= a) and (c > 0)) or ((b >= a) and (c < 0))):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
