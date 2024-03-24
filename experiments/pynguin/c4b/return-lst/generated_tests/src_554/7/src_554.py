def func(*args):
	ret_values = []
	
	word = args[0]
	i = 0
	z = 0
	while (i < len(word)):
	    y = word[i].lower()
	    if ((y != 'a') and (y != 'e') and (y != 'y') and (y != 'u') and (y != 'i') and (y != 'o')):
	        ret_values.append(('.' + word[i].lower()), end='')
	    i += 1

	return ret_values
