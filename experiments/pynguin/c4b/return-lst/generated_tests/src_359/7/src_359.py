def func(*args):
	ret_values = []
	
	x = int(args[0])
	y = 5
	z = 1
	while (x > (y * z)):
	    x -= (y * z)
	    z *= 2
	if ((x - (z * 1)) < 1):
	    ret_values.append('Sheldon')
	elif ((x - (z * 2)) < 1):
	    ret_values.append('Leonard')
	elif ((x - (z * 3)) < 1):
	    ret_values.append('Penny')
	elif ((x - (z * 4)) < 1):
	    ret_values.append('Rajesh')
	elif ((x - (z * 5)) < 1):
	    ret_values.append('Howard')

	return ret_values
