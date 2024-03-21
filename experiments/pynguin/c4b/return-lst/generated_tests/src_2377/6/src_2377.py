def func(*args):
	ret_values = []
	
	chat = args[0]
	hello = []
	count = 0
	for i in chat:
	    if ((count == 0) and (i == 'h')):
	        count += 1
	    elif ((count == 1) and (i == 'e')):
	        count += 1
	    elif ((count == 2) and (i == 'l')):
	        count += 1
	    elif ((count == 3) and (i == 'l')):
	        count += 1
	    elif ((count == 4) and (i == 'o')):
	        count += 1
	    if (count == 5):
	        ret_values.append('YES')
	        exit(0)
	ret_values.append('NO')

	return ret_values
