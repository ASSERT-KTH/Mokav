def func(*args):
	
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
	return(word)
