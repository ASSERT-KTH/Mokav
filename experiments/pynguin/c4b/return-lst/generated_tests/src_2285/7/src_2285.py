def func(*args):
	ret_values = []
	
	word = str(args[0])
	if (word.upper() == word):
	    ret_values.append(word.lower())
	elif (word[1:].upper() == word[1:]):
	    for l in word:
	        if (l.upper() == l):
	            ret_values.append(l.lower(), end='')
	        else:
	            ret_values.append(l.upper(), end='')
	else:
	    ret_values.append(word)

	return ret_values
