def original_func(*args):
	global_list = []
	
	word = args[0]
	if (word.isupper() == True):
	    word = word.lower()
	elif (word[1:].isupper() == True):
	    word = word.capitalize()
	global_list.append(word)
	return global_list