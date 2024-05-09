def original_func(*args):
	global_list = []
	
	text = args[0]
	if (text[0].islower() and text[1:].isupper()):
	    global_list.append('{0}{1}'.format(text[0].upper(), text[1:].lower()))
	elif text.isupper():
	    global_list.append(text.lower())
	elif text[0].islower():
	    global_list.append(text[0].upper())
	else:
	    global_list.append(text)
	return global_list