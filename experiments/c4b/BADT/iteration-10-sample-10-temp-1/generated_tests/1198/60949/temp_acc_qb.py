def patched_func(*args):
	global_list = []
	
	word = args[0]
	instruction = False
	for i in range(len(word)):
	    if ((word[i] == 'H') or (word[i] == 'Q') or (word[i] == '9')):
	        instruction = True
	        break
	if instruction:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list