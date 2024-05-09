def original_func(*args):
	global_list = []
	
	line = args[0]
	counter = 0
	counter1 = 0
	ans = 'NO'
	for a in range(len(line)):
	    if (int(line[a]) == 1):
	        counter += 1
	        counter1 = 0
	    if ((counter == 7) or (counter1 == 7)):
	        ans = 'YES'
	        break
	    else:
	        counter1 += 1
	        counter = 0
	global_list.append(ans)
	return global_list