def original_func(*args):
	global_list = []
	
	s = args[0]
	n = len(s)
	i = 0
	cnt = 0
	flag = 1
	while (i < n):
	    if ((i < (n - 1)) and (s[i] == 'V') and (s[(i + 1)] == 'K')):
	        cnt += 1
	        i += 2
	    elif ((i < (n - 1)) and (s[i] == 'V') and (s[(i + 1)] == 'V') and flag):
	        cnt += 1
	        i += 2
	        flag = 0
	    elif ((i < (n - 1)) and (s[i] == 'K') and (s[(i + 1)] == 'K') and flag):
	        cnt += 1
	        i += 2
	        flag = 0
	    else:
	        i += 1
	global_list.append(cnt)
	return global_list