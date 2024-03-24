def func(*args):
	ret_values = []
	
	i = args[0]
	if ((i[0] == i[0].lower()) and (i[1:] == i[1:].upper())):
	    ret_values.append((i[0].upper() + i[1:].lower()))
	elif (i.upper() == i):
	    ret_values.append(i.lower())
	else:
	    ret_values.append(i)

	return ret_values
