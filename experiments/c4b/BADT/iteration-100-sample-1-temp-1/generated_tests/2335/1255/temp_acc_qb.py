def patched_func(*args):
	global_list = []
	
	s = args[0]
	len_s = len(s)
	t = 'hello'
	j = 0
	count = 0
	for i in t:
	    while True:
	        if (j == len_s):
	            break
	        elif (i == s[j]):
	            count += 1
	            j += 1
	            break
	        elif (i != s[j]):
	            j += 1
	if (count == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list