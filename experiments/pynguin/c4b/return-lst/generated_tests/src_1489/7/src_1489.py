def func(*args):
	ret_values = []
	
	a = args[0]
	if ((a[0].islower() and a[1:].isupper()) or (a.islower() and (len(a) == 1))):
	    ret_values.append((a[0].upper() + a[1:].lower()))
	elif a.isupper():
	    ret_values.append(a.lower())
	else:
	    ret_values.append(a)

	return ret_values
