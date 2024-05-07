def original_func(*args):
	global_list = []
	
	s = str(args[0])
	list1 = ['A', 'E', 'I', 'O', 'U']
	m = 0
	c = (- 100000)
	for i in range(len(s)):
	    if (s[i] in list1):
	        if (c < 0):
	            c = i
	            m = (i + 1)
	        else:
	            if ((i - c) > m):
	                m = (i - c)
	            c = i
	if (c == (- 100000)):
	    global_list.append((len(s) + 1))
	else:
	    global_list.append(max(m, ((len(s) - 1) - c)))
	return global_list