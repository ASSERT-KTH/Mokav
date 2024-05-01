def patched_func(*args):
	global_list = []
	
	w = []
	s = args[0]
	w.append(s)
	wordlength = len(s)
	s = (s + s[0:(wordlength - 1)])
	for i in range(1, wordlength):
	    word = s[i:(i + wordlength)]
	    if (word not in w):
	        w.append(word)
	global_list.append(len(w))
	return global_list