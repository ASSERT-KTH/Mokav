def patched_func(*args):
	global_list = []
	
	word = args[0]
	capital = 0
	small = 0
	for i in range(len(word)):
	    if word[i].isupper():
	        capital += 1
	    else:
	        small += 1
	if (capital > small):
	    global_list.append(word.upper())
	else:
	    global_list.append(word.lower())
	return global_list