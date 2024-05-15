def original_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = False
	for i in range(0, 3):
	    temp = n
	    if (i == 0):
	        temp %= 1234567
	        if ((temp % 1234) == 0):
	            ans = True
	        else:
	            temp %= 123456
	            if ((temp % 1234) == 0):
	                ans = True
	    elif (i == 1):
	        temp %= 123456
	        if ((temp % 1234) == 0):
	            ans = True
	    elif ((temp % 1234) == 0):
	        ans = True
	if ans:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list