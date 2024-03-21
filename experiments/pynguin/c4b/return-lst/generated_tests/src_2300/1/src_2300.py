def func(*args):
	ret_values = []
	
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
	if ((len(word) == 1) and word.islower()):
	    word = word.upper()
	    ret_values.append(word)
	elif ((len(word) == 1) and (not word.islower())):
	    word = word.lower()
	    ret_values.append(word)
	elif (flag and (first == False)):
	    word = word.lower()
	    ret_values.append(word)
	elif (flag and (first == True)):
	    word = (word[0].upper() + word[1:len(word)].lower())
	    ret_values.append(word)
	else:
	    ret_values.append(word)

	return ret_values
