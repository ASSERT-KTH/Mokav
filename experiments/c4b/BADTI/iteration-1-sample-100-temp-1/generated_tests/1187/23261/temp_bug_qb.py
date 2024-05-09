def original_func(*args):
	global_list = []
	
	text = args[0]
	bar = 0
	baz = 0
	if text.isupper():
	    global_list.append(text.lower())
	if (text[0].islower() and text[1:].isupper()):
	    global_list.append((text[0].upper() + text[1:].lower()))
	else:
	    global_list.append(text)
	return global_list