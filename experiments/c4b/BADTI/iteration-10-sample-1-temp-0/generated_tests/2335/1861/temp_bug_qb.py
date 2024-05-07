def original_func(*args):
	global_list = []
	
	hello = 'hello'
	s = args[0]
	count = 0
	for c in s:
	    if (count == 5):
	        break
	    elif (c == hello[count]):
	        count += 1
	global_list.append(('Yes' if (count == 5) else 'NO'))
	return global_list