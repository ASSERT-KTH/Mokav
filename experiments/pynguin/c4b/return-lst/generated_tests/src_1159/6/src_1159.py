def func(*args):
	ret_values = []
	
	import sys
	data = sys.stdin.readline()
	index = int(data)
	if ((index % 3) == 0):
	    ret_values.append(((index * 2) // 3))
	else:
	    multipleOfThree = (index // 3)
	    ret_values.append(((2 * multipleOfThree) + 1))

	return ret_values
