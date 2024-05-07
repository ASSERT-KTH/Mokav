def original_func(*args):
	global_list = []
	
	yr = args[0]
	iter = int(yr)
	flag = 1
	while (flag == 1):
	    unq = 1
	    arr = ([0] * 10)
	    x = list(str(iter))
	    for ch in x:
	        ch = int(ch)
	        if (arr[ch] == 0):
	            arr[ch] = 1
	        else:
	            unq = 0
	    if (unq == 1):
	        global_list.append(str(iter))
	        break
	    iter = (iter + 1)
	return global_list