def patched_func(*args):
	global_list = []
	
	string = args[0]
	string = string.lower()
	t = ''
	for x in range(len(string)):
	    if ((string[x] == 'a') or (string[x] == 'e') or (string[x] == 'i') or (string[x] == 'o') or (string[x] == 'u') or (string[x] == 'y')):
	        continue
	    else:
	        t += ('.' + string[x])
	global_list.append(t)
	return global_list