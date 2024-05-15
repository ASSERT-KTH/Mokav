def patched_func(*args):
	global_list = []
	
	s = args[0]
	lowerCount = 0
	upperCount = 0
	for i in range(len(s)):
	    if ('a' <= s[i] <= 'z'):
	        lowerCount += 1
	    else:
	        upperCount += 1
	if (lowerCount >= upperCount):
	    global_list.append(s.lower())
	else:
	    global_list.append(s.upper())
	return global_list