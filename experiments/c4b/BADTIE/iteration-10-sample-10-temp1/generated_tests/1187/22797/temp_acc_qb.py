def patched_func(*args):
	global_list = []
	
	word = args[0].strip().split(' ')
	res = []
	for (i, s) in enumerate(word):
	    if ((len(word[0]) == 1) and (i == 0)):
	        res.append(s.swapcase())
	    elif s.isupper():
	        res.append(s.lower())
	    elif (s[0].islower() and s[1:].isupper()):
	        res.append(s.title())
	    else:
	        res.append(s)
	global_list.append(' '.join(res))
	return global_list