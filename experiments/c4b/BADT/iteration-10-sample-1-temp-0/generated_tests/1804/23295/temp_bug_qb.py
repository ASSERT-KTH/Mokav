def original_func(*args):
	global_list = []
	
	name_user = str(args[0])
	list_name_user = []
	for item in name_user:
	    list_name_user.append(item)
	n = len(list_name_user)
	for i in range(n):
	    j = (i + 1)
	    while (j < n):
	        if (list_name_user[i] == list_name_user[j]):
	            del list_name_user[j]
	            n -= 1
	            global_list.append(list_name_user)
	        else:
	            j += 1
	if ((n % 2) != 0):
	    global_list.append('IGNORE HIM!')
	else:
	    global_list.append('CHAT WITH HER!')
	return global_list