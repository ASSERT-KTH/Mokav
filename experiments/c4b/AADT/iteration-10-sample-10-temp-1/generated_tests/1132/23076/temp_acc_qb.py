def patched_func(*args):
	global_list = []
	
	string = args[0]
	list1 = []
	num1 = '47'
	for i in string:
	    if (i in num1):
	        list1.append(i)
	        continue
	    elif (i not in num1):
	        break
	if (len(list1) != len(string)):
	    if (((int(string) % 4) == 0) or ((int(string) % 7) == 0) or ((int(string) % 47) == 0)):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list