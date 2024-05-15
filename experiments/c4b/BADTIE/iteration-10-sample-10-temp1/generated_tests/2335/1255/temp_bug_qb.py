def original_func(*args):
	global_list = []
	
	s = args[0]
	len_s = len(s)
	global_list.append(len_s)
	t = 'hello'
	j = 0
	count = 0
	for i in t:
	    while True:
	        if (j == len_s):
	            break
	        elif (i == s[j]):
	            count += 1
	            break
	        j += 1
	global_list.append(count)
	if (count == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list