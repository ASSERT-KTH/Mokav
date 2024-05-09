def original_func(*args):
	global_list = []
	
	a = args[0]
	b = []
	for i in a:
	    b.append(i)
	if (len(b) < 7):
	    global_list.append('NO')
	elif (len(b) >= 7):
	    i = 0
	    while (i <= (len(b) - 7)):
	        if (((((((int(b[i]) + int(b[(i + 1)])) + int(b[(i + 2)])) + int(b[(i + 3)])) + int(b[(i + 4)])) + int(b[(i + 5)])) + (int(b[(i + 6)]) % 7)) == 0):
	            global_list.append('YES')
	            break
	        else:
	            i += 1
	    else:
	        global_list.append('NO')
	return global_list