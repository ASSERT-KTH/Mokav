def func(*args):
	ret_values = []
	
	word = args[0]
	count_upper = sum(map(str.isupper, word))
	count_lower = sum(map(str.islower, word))
	if (count_upper > count_lower):
	    ret_values.append(word.upper())
	else:
	    ret_values.append(word.lower())

	return ret_values
