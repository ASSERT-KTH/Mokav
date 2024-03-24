def func(*args):
	ret_values = []
	
	n = args[0]
	if (n[1:] == n[1:].upper()):
	    if (n[0] == n[0].upper()):
	        ret_values.append(n.lower())
	    else:
	        ret_values.append((n[0].upper() + n[1:].lower()))
	else:
	    ret_values.append(n)

	return ret_values
