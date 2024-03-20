def func(*args):
	
	word = args[0]
	if ((len(word) <= 100) and (len(word) > 0)):
	    if (word[0:].isupper() == True):
	        word = word.lower()
	    elif ((word[0].islower() == True) and (word[1:].isupper() == True)):
	        word = word.swapcase()
	    elif ((len(word) == 1) and word[0].islower()):
	        word = word.swapcase()
	    return(word)
