def original_func(*args):
	global_list = []
	
	a = args[0]
	arr = []
	s = a.lower()
	s1 = s.replace('a', '')
	s2 = s1.replace('e', '')
	s3 = s2.replace('i', '')
	s4 = s3.replace('o', '')
	s5 = s4.replace('u', '')
	for i in range(len(s5)):
	    arr.append('.')
	    arr.append(str(s5[i]))
	global_list.append(''.join((str(x) for x in arr)))
	return global_list