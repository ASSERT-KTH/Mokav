def original_func(*args):
	global_list = []
	
	st = args[0]
	number = 0
	for c in st:
	    if ((c == '4') or (c == '7')):
	        number += 1
	        global_list.append(number)
	if ((number == 4) or (number == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list