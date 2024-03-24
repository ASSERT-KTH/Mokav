def func(*args):
	ret_values = []
	
	import sys
	watermelon = int(args[0])
	if (((watermelon % 2) == 0) and (watermelon > 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
