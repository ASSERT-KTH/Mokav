def func(*args):
	ret_values = []
	
	u = int(args[0])
	if (u == 1):
	    ret_values.append(1)
	if (2 <= u <= 5):
	    if (u == 3):
	        ret_values.append(5)
	    else:
	        ret_values.append(3)
	if (6 <= u <= 13):
	    ret_values.append(5)
	if (14 <= u <= 25):
	    ret_values.append(7)
	if (26 <= u <= 41):
	    ret_values.append(9)
	if (42 <= u <= 61):
	    ret_values.append(11)
	if (62 <= u <= 85):
	    ret_values.append(13)
	if (86 <= u <= 100):
	    ret_values.append(15)

	return ret_values
