def original_func(*args):
	global_list = []
	
	word = args[0]
	upper = 0
	lower = 0
	for char in word:
	    if (char == char.upper()):
	        upper += 1
	    else:
	        lower += 1
	    global_list.append(lower, upper)
	if (lower >= upper):
	    word = word.lower()
	elif (lower < upper):
	    word = word.upper()
	global_list.append(word)
	return global_list