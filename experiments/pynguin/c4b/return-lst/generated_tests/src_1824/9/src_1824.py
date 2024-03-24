def func(*args):
	ret_values = []
	
	line = args[0]
	counter = 0
	counter1 = 0
	ans = 'NO'
	for a in range(len(line)):
	    if (int(line[a]) == 1):
	        counter += 1
	        counter1 = 0
	    else:
	        counter1 += 1
	        counter = 0
	    if ((counter == 7) or (counter1 == 7)):
	        ans = 'YES'
	        break
	ret_values.append(ans)

	return ret_values
