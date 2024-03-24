def func(*args):
	ret_values = []
	
	maximum = max([int(x) for x in args[0].split()])
	if (maximum == 1):
	    ret_values.append('1/1')
	elif (maximum == 2):
	    ret_values.append('5/6')
	elif (maximum == 3):
	    ret_values.append('2/3')
	elif (maximum == 4):
	    ret_values.append('1/2')
	elif (maximum == 5):
	    ret_values.append('1/3')
	else:
	    ret_values.append('1/6')

	return ret_values
