def original_func(*args):
	global_list = []
	
	word = args[0]
	count = 0
	output = ''
	for x in word:
	    if ((count == 0) and x.islower()):
	        x = x.upper()
	    elif x.isupper():
	        x = x.lower()
	    else:
	        global_list.append(word)
	        break
	    count += 1
	    output += x
	if (count == (len(word) - 1)):
	    global_list.append(output)
	return global_list