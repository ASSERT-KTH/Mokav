def original_func(*args):
	global_list = []
	
	s = args[0]
	s = list(s)
	count = 0
	count1 = 0
	for x in s:
	    if x.isupper:
	        count += 1
	    elif x.islower:
	        count1 += 1
	s = ''.join(s)
	if ((count == count1) or (count1 > count)):
	    global_list.append(s.lower())
	elif (count > count1):
	    global_list.append(s.upper())
	return global_list