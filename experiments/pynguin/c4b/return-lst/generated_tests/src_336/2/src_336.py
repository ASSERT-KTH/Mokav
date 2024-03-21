def func(*args):
	ret_values = []
	
	n = int(args[0])
	x = 0
	total = 0
	while (1 > 0):
	    if (total >= n):
	        break
	    s = total
	    total = (total + (5 * pow(2, x)))
	    x = (x + 1)
	t = ((n - s) / pow(2, (x - 1)))
	if (t <= 1):
	    ret_values.append('Sheldon')
	elif ((t > 1) and (t <= 2)):
	    ret_values.append('Leonard')
	elif ((t > 2) and (t <= 3)):
	    ret_values.append('Penny')
	elif ((t > 3) and (t <= 4)):
	    ret_values.append('Rajesh')
	elif ((t > 4) and (t <= 5)):
	    ret_values.append('Howard')

	return ret_values
