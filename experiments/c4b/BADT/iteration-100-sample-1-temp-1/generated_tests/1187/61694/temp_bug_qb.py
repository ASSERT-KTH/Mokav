def original_func(*args):
	global_list = []
	
	word = args[0]
	flag = 0
	first = False
	if word[0].islower():
	    first = True
	for i in range(1, len(word)):
	    if (not word[i].islower()):
	        flag = 1
	    else:
	        flag = 0
	        break
	if (len(word) == 1):
	    word = word.upper()
	    global_list.append(word)
	elif (flag and (first == False)):
	    word = word.lower()
	    global_list.append(word)
	elif (flag and (first == True)):
	    word = (word[0].upper() + word[1:len(word)].lower())
	    global_list.append(word)
	else:
	    global_list.append(word)
	return global_list