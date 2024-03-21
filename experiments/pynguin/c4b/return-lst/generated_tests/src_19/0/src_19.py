def func(*args):
	ret_values = []
	
	import sys
	n = int(sys.stdin.readline())
	a = 1378
	endVals = [8, 4, 2, 6]
	if (n != 0):
	    ret_values.append(endVals[((n % 4) - 1)])
	else:
	    ret_values.append(1)

	return ret_values
