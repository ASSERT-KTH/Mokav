def func(*args):
	ret_values = []
	
	a = args[0]
	b = list(a)
	if (len(b) == 1):
	    if (a == a.upper()):
	        ret_values.append(a.lower())
	    else:
	        ret_values.append(a.upper())
	elif (a.lower() == a):
	    ret_values.append(a)
	elif (a.upper() == a):
	    ret_values.append(a.lower())
	elif (b[0].lower() == b[0]):
	    c = a[1:]
	    if (c.upper() == c):
	        ret_values.append((b[0].upper() + c.lower()))
	    else:
	        ret_values.append(a)
	elif (b[0].upper() == b[0]):
	    ret_values.append(a)

	return ret_values
