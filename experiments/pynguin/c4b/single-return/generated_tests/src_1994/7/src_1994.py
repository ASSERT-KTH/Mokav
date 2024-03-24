def func(*args):
	
	word = list(args[0])
	comb = []
	for i in range(len(word)):
	    l = word[(- 1)]
	    del word[(- 1)]
	    word = ([l] + word)
	    str1 = ''.join(word)
	    comb.append(str1)
	return(len(set(comb)))
