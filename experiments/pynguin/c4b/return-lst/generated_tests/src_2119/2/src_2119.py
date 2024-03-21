def func(*args):
	ret_values = []
	
	n = args[0]
	n_1 = n[1:]
	if (n.isupper() == True):
	    ret_values.append(n.lower())
	elif ((n_1.isupper() == True) and (n[:1].islower() == True)):
	    ret_values.append(n.capitalize())
	elif ((n_1 == '') and (n[:1].islower() == True)):
	    ret_values.append(n.capitalize())
	else:
	    ret_values.append(n)

	return ret_values
