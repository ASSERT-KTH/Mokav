def patched_func(*args):
	global_list = []
	
	text = args[0]
	if text.isupper():
	    global_list.append(text.lower())
	elif (text[0].islower() and text[1:].isupper()):
	    global_list.append((text[0].upper() + text[1:].lower()))
	elif (len(text) == 1):
	    if text.isupper():
	        global_list.append(text.lower())
	    else:
	        global_list.append(text.upper())
	else:
	    global_list.append(text)
	return global_list