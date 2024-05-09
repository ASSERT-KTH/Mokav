def original_func(*args):
	global_list = []
	
	string = args[0]
	ln = len(string)
	if (ln == 1):
	    global_list.append(0)
	elif (ln == 2):
	    if (string != 'KV'):
	        global_list.append(1)
	    else:
	        global_list.append(0)
	else:
	    chang = ['VVV', 'KKK']
	    add = 0
	    for i in chang:
	        if string.count(i):
	            add = 1
	            break
	    global_list.append((string.count('VK') + add))
	return global_list