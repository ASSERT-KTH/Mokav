def func(*args):
	
	input_word = args[0]
	exists = True
	for (i, c) in enumerate('hello'):
	    if (input_word.find(c) >= 0):
	        input_word = input_word[(input_word.index(c) + 1):]
	    else:
	        exists = False
	        break
	return(((exists and 'YES') or 'NO'))
