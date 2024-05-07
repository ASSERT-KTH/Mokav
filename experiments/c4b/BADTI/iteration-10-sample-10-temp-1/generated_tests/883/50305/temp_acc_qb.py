def patched_func(*args):
	global_list = []
	
	word = list(args[0])
	comb = []
	for i in range(len(word)):
	    l = word[(- 1)]
	    del word[(- 1)]
	    word = ([l] + word)
	    str1 = ''.join(word)
	    comb.append(str1)
	global_list.append(len(set(comb)))
	return global_list