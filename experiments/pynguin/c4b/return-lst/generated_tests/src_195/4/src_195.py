def func(*args):
	ret_values = []
	
	word = args[0]
	check = False
	for i in range(0, len(word)):
	    if ((word[i] == 'H') or (word[i] == 'Q') or (word[i] == '9')):
	        check = True
	if (check == True):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
