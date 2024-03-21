def func(*args):
	ret_values = []
	
	lisa = args[0]
	if (lisa == lisa.upper()):
	    ret_values.append(lisa.lower())
	elif ((lisa == (lisa[0].lower() + lisa[1:].upper())) and (len(lisa) > 1)):
	    ret_values.append((lisa[0].upper() + lisa[1:].lower()))
	elif (len(lisa) == 1):
	    ret_values.append(lisa.upper())
	else:
	    ret_values.append(lisa)

	return ret_values
