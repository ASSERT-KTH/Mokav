def func(*args):
	ret_values = []
	
	x = int(args[0])
	if (x == 3):
	    ret_values.append(5)
	elif (x <= 1):
	    ret_values.append(1)
	elif (x <= 5):
	    ret_values.append(3)
	elif (x <= 13):
	    ret_values.append(5)
	elif (x <= 25):
	    ret_values.append(7)
	elif (x <= 41):
	    ret_values.append(9)
	elif (x <= 61):
	    ret_values.append(11)
	elif (x <= 85):
	    ret_values.append(13)
	else:
	    ret_values.append(15)

	return ret_values
