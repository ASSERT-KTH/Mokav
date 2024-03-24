def func(*args):
	ret_values = []
	
	word = args[0]
	instruction = False
	for i in range(len(word)):
	    if ((word[i] == 'H') or (word[i] == 'Q') or (word[i] == '9')):
	        instruction = True
	        break
	if instruction:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
