def original_func(*args):
	global_list = []
	
	s = args[0]
	li = ['H', 'Q', '9']
	flag = True
	for i in li:
	    if (i in s):
	        global_list.append('YES')
	        flag = False
	        break
	if ((len(s) > 1) and (s[(- 1)] is '+')):
	    global_list.append('YES')
	    flag = False
	if flag:
	    global_list.append('NO')
	return global_list