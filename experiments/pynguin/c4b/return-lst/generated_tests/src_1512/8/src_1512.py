def func(*args):
	ret_values = []
	
	text = args[0]
	if text.isupper():
	    ret_values.append(text.lower())
	elif (text[0].islower() and text[1:].isupper()):
	    ret_values.append((text[0].upper() + text[1:].lower()))
	elif (len(text) == 1):
	    if text.isupper():
	        ret_values.append(text.lower())
	    else:
	        ret_values.append(text.upper())
	else:
	    ret_values.append(text)

	return ret_values
