def original_func(*args):
	global_list = []
	
	s = args[0]
	b = 0
	b_i = (- 1)
	for (i, c) in enumerate(s):
	    t = 0
	    if (i > 0):
	        if (s[(i - 1)] == s[i]):
	            t += 1
	            if ((i < (len(s) - 1)) and (s[(i + 1)] != s[i])):
	                t -= 1
	            else:
	                t += 1
	        if (t > b):
	            b_i = i
	            b = t
	if (b_i != (- 1)):
	    global_list.append(((s[0:b_i] + ('V' if (s[b_i] == 'K') else 'K')) + ('' if (b_i == (len(s) - 1)) else s[(b_i + 1):])).count('VK'))
	else:
	    global_list.append(s.count('VK'))
	return global_list