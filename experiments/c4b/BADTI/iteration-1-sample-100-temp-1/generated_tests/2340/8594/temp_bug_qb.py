def original_func(*args):
	global_list = []
	
	s = args[0]
	s1 = s.lower()
	s2 = s.upper()
	set1 = (set(s) & set(s1))
	set2 = (set(s) & set(s2))
	if (len(set2) > len(set1)):
	    global_list.append(s2)
	else:
	    global_list.append(s1)
	return global_list