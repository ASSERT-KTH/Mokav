def original_func(*args):
	global_list = []
	
	word = args[0]
	if ((len(word) <= 100) and (len(word) > 0)):
	    if (word[0:].isupper() == True):
	        word = word.lower()
	    elif ((word[0].islower() == True) and (word[1:].isupper() == True)):
	        word = word.swapcase()
	    elif (word[0].islower() == True):
	        word = word.swapcase()
	    global_list.append(word)
	return global_list