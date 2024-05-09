def original_func(*args):
	global_list = []
	
	k = 0
	j = 0
	word = args[0]
	for i in range(len(word)):
	    if ((word[i] == 'H') or (word[i] == 'Q') or (word == '9')):
	        k = (k + 1)
	    else:
	        j = (j + 1)
	if (k >= 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list