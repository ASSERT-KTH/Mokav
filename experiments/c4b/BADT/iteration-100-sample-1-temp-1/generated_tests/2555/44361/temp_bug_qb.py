def original_func(*args):
	global_list = []
	
	Location = str(args[0])
	i = 0
	k = 1
	for i in range((len(Location) - 1)):
	    if (Location[i] == Location[(i + 1)]):
	        k += 1
	    elif (k < 7):
	        k = 1
	    else:
	        global_list.append('YES')
	        break
	if (k < 7):
	    global_list.append('NO')
	return global_list