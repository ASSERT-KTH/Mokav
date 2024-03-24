def func(*args):
	ret_values = []
	
	b = args[0]
	count = 0
	for i in range((len(b) - 1)):
	    if (b[i] == b[(i + 1)]):
	        count += 1
	    else:
	        count = 0
	    if (count > 5):
	        break
	if (count < 6):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
