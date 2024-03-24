def func(*args):
	ret_values = []
	
	a = int(args[0])
	i = 0
	while ((5 * ((2 ** i) - 1)) < a):
	    i += 1
	if ((((5 * ((2 ** i) - 1)) - (5 * (2 ** (i - 1)))) + 1) <= a < (((5 * ((2 ** i) - 1)) - (4 * (2 ** (i - 1)))) + 1)):
	    ret_values.append('Sheldon')
	elif ((((5 * ((2 ** i) - 1)) - (4 * (2 ** (i - 1)))) + 1) <= a < (((5 * ((2 ** i) - 1)) - (3 * (2 ** (i - 1)))) + 1)):
	    ret_values.append('Leonard')
	elif ((((5 * ((2 ** i) - 1)) - (3 * (2 ** (i - 1)))) + 1) <= a < (((5 * ((2 ** i) - 1)) - (2 * (2 ** (i - 1)))) + 1)):
	    ret_values.append('Penny')
	elif ((((5 * ((2 ** i) - 1)) - (2 * (2 ** (i - 1)))) + 1) <= a < (((5 * ((2 ** i) - 1)) - (1 * (2 ** (i - 1)))) + 1)):
	    ret_values.append('Rajesh')
	elif ((((5 * ((2 ** i) - 1)) - (2 ** (i - 1))) + 1) <= a < ((5 * ((2 ** i) - 1)) + 1)):
	    ret_values.append('Howard')

	return ret_values
