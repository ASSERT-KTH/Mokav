def func(*args):
	ret_values = []
	
	word = args[0]
	capital = 0
	small = 0
	for i in range(len(word)):
	    if word[i].isupper():
	        capital += 1
	    else:
	        small += 1
	if (capital > small):
	    ret_values.append(word.upper())
	else:
	    ret_values.append(word.lower())

	return ret_values
