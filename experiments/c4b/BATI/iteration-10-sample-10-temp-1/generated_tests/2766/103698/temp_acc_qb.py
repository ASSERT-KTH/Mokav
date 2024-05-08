def patched_func(*args):
	global_list = []
	
	string = args[0]
	razl = 0
	for i in range((len(string) // 2)):
	    if (string[i] != string[((- i) - 1)]):
	        razl += 1
	if (razl > 1):
	    global_list.append('NO')
	elif (razl == 1):
	    global_list.append('YES')
	elif ((len(string) % 2) == 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list