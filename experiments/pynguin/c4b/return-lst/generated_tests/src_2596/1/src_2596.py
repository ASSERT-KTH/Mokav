def func(*args):
	ret_values = []
	
	a = int(args[0])
	sstring = []
	if (a % 2):
	    sstring.append('7')
	else:
	    a = a
	if (a % 2):
	    a = (a - 3)
	else:
	    a = a
	for i in range((a // 2)):
	    sstring.append('1')
	ret_values.append(''.join(sstring))

	return ret_values
