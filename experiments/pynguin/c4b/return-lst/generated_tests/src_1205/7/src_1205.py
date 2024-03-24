def func(*args):
	ret_values = []
	
	import sys
	import math
	(al, ar) = [int(x) for x in sys.stdin.readline().split()]
	(bl, br) = [int(x) for x in sys.stdin.readline().split()]
	if (((br >= (al - 1)) and (br <= (((al - 1) * 2) + 4))) or ((bl >= (ar - 1)) and (bl <= (((ar - 1) * 2) + 4)))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
