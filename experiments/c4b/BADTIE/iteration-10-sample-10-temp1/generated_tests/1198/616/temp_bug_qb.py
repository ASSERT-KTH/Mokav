def original_func(*args):
	global_list = []
	
	word = args[0]
	check = False
	for i in range(0, len(word)):
	    if ((word[i] == 'H') or (word[i] == 'Q') or (word[i] == '9') or (word[i] == '+')):
	        check = True
	if (check == True):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list