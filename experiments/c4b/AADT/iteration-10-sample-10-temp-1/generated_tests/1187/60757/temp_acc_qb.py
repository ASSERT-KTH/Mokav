def patched_func(*args):
	global_list = []
	
	str = args[0]
	flag = 0
	if str.isupper():
	    global_list.append(str.lower())
	elif str[0].islower():
	    if (len(str) == 1):
	        global_list.append(str.upper())
	    else:
	        for i in str[1:]:
	            if i.islower():
	                global_list.append(str)
	                flag = 1
	                break
	        if (flag == 0):
	            global_list.append(str.swapcase())
	else:
	    global_list.append(str)
	return global_list