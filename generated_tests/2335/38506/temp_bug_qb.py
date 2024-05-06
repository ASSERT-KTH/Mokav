def original_func(*args):
	global_list = []
	
	input_word = args[0]
	exists = True
	for (i, c) in enumerate('hello'):
	    global_list.append(input_word)
	    if (input_word.find(c) >= 0):
	        input_word = input_word[(input_word.index(c) + 1):]
	    else:
	        exists = False
	        break
	global_list.append(((exists and 'YES') or 'NO'))
	return global_list