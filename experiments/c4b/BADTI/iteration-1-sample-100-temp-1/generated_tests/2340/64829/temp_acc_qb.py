def patched_func(*args):
	global_list = []
	
	word = args[0]
	count_upper = sum(map(str.isupper, word))
	count_lower = sum(map(str.islower, word))
	if (count_upper > count_lower):
	    global_list.append(word.upper())
	else:
	    global_list.append(word.lower())
	return global_list