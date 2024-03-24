def func(*args):
	ret_values = []
	
	a = int(args[0])
	if (a == 1):
	    ret_values.append(2)
	if (a == 3):
	    ret_values.append(1)
	if (a == 2):
	    ret_values.append(3)
	if (a == 4):
	    ret_values.append(2)
	if (a == 5):
	    ret_values.append(1)

	return ret_values
