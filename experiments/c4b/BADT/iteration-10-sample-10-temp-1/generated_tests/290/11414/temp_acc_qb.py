def patched_func(*args):
	global_list = []
	
	(a, b, c) = list(map(int, args[0].split()))
	x = c
	flag = 'No'
	if (((c % a) == 0) or ((c % b) == 0)):
	    flag = 'Yes'
	else:
	    while (x > 0):
	        x = (x - a)
	        if (((x % b) == 0) and (x > 0)):
	            flag = 'Yes'
	            break
	    if (flag == 'No'):
	        x = c
	        while (x > 0):
	            x = (x - b)
	            if (((x % a) == 0) and (x > 0)):
	                flag = 'Yes'
	                break
	global_list.append(flag)
	return global_list