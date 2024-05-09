def original_func(*args):
	global_list = []
	
	s = args[0]
	cnt1 = cnt2 = 0
	for i in s:
	    if s.islower():
	        cnt1 += 1
	    else:
	        cnt2 += 1
	if (cnt2 > cnt1):
	    s = s.upper()
	else:
	    s = s.lower()
	global_list.append(s)
	return global_list