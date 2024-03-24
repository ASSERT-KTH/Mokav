def func(*args):
	ret_values = []
	
	text = args[0]
	if (text[0].islower() and text[1:].isupper()):
	    ret_values.append('{0}{1}'.format(text[0].upper(), text[1:].lower()))
	elif text.isupper():
	    ret_values.append(text.lower())
	elif ((len(text) == 1) and text[0].islower()):
	    ret_values.append(text[0].upper())
	else:
	    ret_values.append(text)

	return ret_values
