def func(*args):
	ret_values = []
	
	x = args[0]
	y = x.capitalize()
	caps = x.upper()
	first = x[0]
	last = x[1:]
	nocaps = x.lower()
	if ((x != caps) and (x != nocaps)):
	    if ((x == y) or ((first == first.lower()) and (last == last.upper()))):
	        ret_values.append(y)
	    else:
	        ret_values.append(x)
	elif ((len(x) == 1) and (x == nocaps)):
	    ret_values.append(caps)
	elif ((len(x) == 1) and (x == caps)):
	    ret_values.append(nocaps)
	elif (x == caps):
	    ret_values.append(nocaps)
	elif (x == nocaps):
	    ret_values.append(x)

	return ret_values
