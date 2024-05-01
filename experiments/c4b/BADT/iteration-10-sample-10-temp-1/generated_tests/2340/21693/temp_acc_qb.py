def patched_func(*args):
	global_list = []
	
	word = args[0]
	maj = 0
	mini = 0
	for i in range(len(word)):
	    if (word[i].islower() == True):
	        mini = (mini + 1)
	    elif (word[i].isupper() == True):
	        maj = (maj + 1)
	if (maj > mini):
	    global_list.append(word.upper())
	else:
	    global_list.append(word.lower())
	return global_list