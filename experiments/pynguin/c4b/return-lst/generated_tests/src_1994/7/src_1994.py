def func(*args):
	ret_values = []
	
	word = list(args[0])
	comb = []
	for i in range(len(word)):
	    l = word[(- 1)]
	    del word[(- 1)]
	    word = ([l] + word)
	    str1 = ''.join(word)
	    comb.append(str1)
	ret_values.append(len(set(comb)))

	return ret_values
