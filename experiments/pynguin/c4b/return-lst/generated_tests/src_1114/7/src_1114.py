def func(*args):
	ret_values = []
	
	word = args[0]
	if (len(word) == 1):
	    if (word.isupper() == True):
	        word = word.lower()
	    else:
	        word = word.upper()
	elif (word.isupper() == True):
	    word = word.lower()
	elif (word[1:].isupper() == True):
	    word = word.capitalize()
	ret_values.append(word)

	return ret_values
