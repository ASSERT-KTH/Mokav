def func(*args):
	ret_values = []
	
	n = args[0]
	if (len(n) == 1):
	    if n.isupper():
	        ret_values.append(n.lower())
	    else:
	        ret_values.append(n.upper())
	    exit(0)
	if n.isupper():
	    ret_values.append(n.lower())
	elif (n[0].islower() and n[1:].isupper()):
	    ret_values.append((n[0].upper() + n[1:].lower()))
	else:
	    ret_values.append(n)

	return ret_values
