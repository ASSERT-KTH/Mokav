def original_func(*args):
	global_list = []
	
	s = args[0]
	num = 0
	p = 0
	for i in range((len(s) - 1)):
	    if ((s[i] == 'V') and (s[(i + 1)] == 'K')):
	        num += 1
	    if (((i + 2) < len(s)) and (s[i] == 'V') and (s[(i + 1)] == 'V') and (s[(i + 2)] == 'V')):
	        p = 1
	if ((len(s) > 1) and (s[(- 1)] == 'V') and (s[(- 2)] == 'V')):
	    p = 1
	global_list.append((num + p))
	return global_list