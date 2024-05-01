def original_func(*args):
	global_list = []
	
	s = args[0]
	s = list(s)
	c = ['', 'h', 'e', 'l', 'l', 'o']
	count = 1
	for x in s:
	    if (x == c[count]):
	        count += 1
	    elif (x == c[(count - 1)]):
	        pass
	    elif ((x != c[count]) and (count > 1)):
	        count = 0
	    if (count == 5):
	        break
	if (count == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list