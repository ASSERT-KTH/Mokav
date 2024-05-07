def patched_func(*args):
	global_list = []
	
	str = args[0]
	index = int((len(str) / 2))
	count = 0
	for i in range(0, index):
	    if (not (str[i] == str[((- i) - 1)])):
	        count += 1
	if (count == 1):
	    global_list.append('YES')
	elif ((count == 0) and ((len(str) % 2) == 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list