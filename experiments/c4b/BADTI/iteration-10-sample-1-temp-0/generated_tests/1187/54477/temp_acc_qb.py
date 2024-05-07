def patched_func(*args):
	global_list = []
	
	text = args[0]
	if text.isupper():
	    global_list.append(text.lower())
	elif ((text[:1] == text[:1].lower()) and (text[1:] == text[1:].upper())):
	    text = text.lower()
	    big = text[:1].upper()
	    global_list.append((big + text[1:]))
	else:
	    global_list.append(text)
	return global_list