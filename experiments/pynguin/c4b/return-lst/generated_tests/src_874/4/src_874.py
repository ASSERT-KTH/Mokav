def func(*args):
	ret_values = []
	
	x = int(args[0])
	if (x <= 7):
	    if (x == 1):
	        ret_values.append(0, 1)
	    elif (x == 6):
	        ret_values.append(1, 2)
	    elif (x == 7):
	        ret_values.append(2, 2)
	    else:
	        ret_values.append(0, 2)
	if (x > 7):
	    if ((x % 7) == 0):
	        ret_values.append(int((2 * (x / 7))), int((2 * (x / 7))))
	    elif ((x % 7) == 6):
	        ret_values.append(int((2 * (x / 7))), (int((2 * (x / 7))) + 1))
	    elif ((x % 7) == 1):
	        ret_values.append((2 * int((x / 7))), ((2 * int((x / 7))) + 1))
	    else:
	        ret_values.append((2 * int((x / 7))), ((2 * int((x / 7))) + 2))

	return ret_values
