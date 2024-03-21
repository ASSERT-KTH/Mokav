def func(*args):
	ret_values = []
	
	ip = args[0].strip()
	old_key = None
	count = 0
	flag = 0
	for c in ip:
	    if (old_key == None):
	        old_key = c
	        count = 1
	    elif (old_key == c):
	        count += 1
	    else:
	        if (count >= 7):
	            flag = 1
	            break
	        old_key = c
	        count = 1
	if (flag == 0):
	    if (count >= 7):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif (flag == 1):
	    ret_values.append('YES')

	return ret_values
