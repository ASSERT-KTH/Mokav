def patched_func(*args):
	global_list = []
	
	K = int(args[0])
	L = int(args[1])
	importance = 0
	flag = 0
	for i in range(1, 65):
	    if ((K ** i) == L):
	        flag = 1
	        importance = i
	        break
	if (flag == 1):
	    global_list.append('YES')
	    global_list.append((importance - 1))
	else:
	    global_list.append('NO')
	return global_list