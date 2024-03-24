def func(*args):
	ret_values = []
	
	(x, y, z) = map(int, args[0].split())
	if ((x > 0) and (x <= (10 ** 9)) and (y >= 0) and (y <= (10 ** 9)) and (z >= 0) and (z <= (10 ** 9)) and ((y + z) > 0)):
	    if ((x > y) and (x > z)):
	        ret_values.append((- 1))
	    elif ((y > x) and ((y % x) != 0) and (x > z)):
	        ret_values.append((- 1))
	    elif ((x > y) and ((z % x) != 0) and (z > x)):
	        ret_values.append((- 1))
	    else:
	        ret_values.append(((y // x) + (z // x)))
	else:
	    ret_values.append((- 1))

	return ret_values
