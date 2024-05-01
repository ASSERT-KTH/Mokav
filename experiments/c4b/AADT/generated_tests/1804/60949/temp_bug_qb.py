def original_func(*args):
	global_list = []
	
	username = args[0]
	num = 0
	for i in range(len(username)):
	    for a in range(0, i):
	        if (username[i] == username[a]):
	            num -= 1
	    num += 1
	if ((num % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list