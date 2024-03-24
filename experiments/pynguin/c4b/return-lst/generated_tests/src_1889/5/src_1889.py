def func(*args):
	ret_values = []
	
	import sys
	num = int(args[0])
	left = (num % 4)
	if (num == 0):
	    ret_values.append(1)
	elif ((left % 4) == 2):
	    ret_values.append(4)
	elif ((left % 4) == 0):
	    ret_values.append(6)
	elif ((left % 4) == 1):
	    ret_values.append(8)
	elif ((left % 4) == 3):
	    ret_values.append(2)

	return ret_values
