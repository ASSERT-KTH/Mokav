def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	n += 1
	while 1:
	    s = str(n)
	    lst = []
	    flag = True
	    for i in s:
	        if (i in lst):
	            flag = False
	        else:
	            lst.append(i)
	    if flag:
	        global_list.append(n)
	        break
	    n += 1
	return global_list