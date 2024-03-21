def func(*args):
	ret_values = []
	
	word = args[0]
	maj = 0
	mini = 0
	for i in range(len(word)):
	    if (word[i].islower() == True):
	        mini = (mini + 1)
	    elif (word[i].isupper() == True):
	        maj = (maj + 1)
	if (maj > mini):
	    ret_values.append(word.upper())
	else:
	    ret_values.append(word.lower())

	return ret_values
