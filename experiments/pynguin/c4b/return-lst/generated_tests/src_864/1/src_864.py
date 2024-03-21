def func(*args):
	ret_values = []
	
	word = args[0]
	if (word == (word[:1].lower() + word[1:].upper())):
	    ret_values.append((word[:1].upper() + word[1:].lower()))
	elif (word == word[0:].upper()):
	    ret_values.append(word[0:].lower())
	else:
	    ret_values.append(word)

	return ret_values
