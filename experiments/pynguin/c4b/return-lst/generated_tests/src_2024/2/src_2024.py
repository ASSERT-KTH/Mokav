def func(*args):
	ret_values = []
	
	word = args[0]
	upper = 0
	lower = 0
	for char in word:
	    if (char == char.upper()):
	        upper += 1
	    else:
	        lower += 1
	if (lower >= upper):
	    word = word.lower()
	elif (lower < upper):
	    word = word.upper()
	ret_values.append(word)

	return ret_values
