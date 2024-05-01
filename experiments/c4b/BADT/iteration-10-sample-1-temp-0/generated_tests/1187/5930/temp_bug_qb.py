def original_func(*args):
	global_list = []
	
	word = args[0]
	if (word == (word[:1].lower() + word[1:].upper())):
	    global_list.append((word[:1].upper() + word[1:].lower()))
	if (word == word[:].upper()):
	    global_list.append(word[:].lower())
	else:
	    global_list.append(word)
	return global_list