def func(*args):
	ret_values = []
	
	str = args[0]
	index = int((len(str) / 2))
	count = 0
	for i in range(0, index):
	    if (not (str[i] == str[((- i) - 1)])):
	        count += 1
	if (count == 1):
	    ret_values.append('YES')
	elif ((count == 0) and ((len(str) % 2) == 1)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
