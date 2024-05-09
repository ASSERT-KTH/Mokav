def patched_func(*args):
	global_list = []
	
	s = args[0]
	res = 0
	if (len(s) < 2):
	    global_list.append(0)
	else:
	    for i in range((len(s) - 1)):
	        if ((s[i] == 'V') and (s[(i + 1)] == 'K')):
	            res += 1
	    if (('VVV' in s) or (s[(- 2):] == 'VV')):
	        res += 1
	    elif (('KKK' in s) or (s[:2] == 'KK')):
	        res += 1
	    global_list.append(res)
	return global_list