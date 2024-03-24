def func(*args):
	ret_values = []
	
	k = 0
	j = 0
	word = args[0]
	for i in range(len(word)):
	    if ((word[i] == 'H') or (word[i] == 'Q') or (word[i] == '9')):
	        k = (k + 1)
	    else:
	        j = (j + 1)
	if (k >= 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
