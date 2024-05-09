def original_func(*args):
	global_list = []
	
	w = []
	s = args[0]
	w.append(s)
	wordlength = len(s)
	s = (s + s[0:(wordlength - 1)])
	global_list.append(s)
	for i in range(1, wordlength):
	    word = s[i:(i + wordlength)]
	    global_list.append(word)
	    if (word not in w):
	        w.append(word)
	global_list.append(len(w))
	return global_list