def func(*args):
	ret_values = []
	
	string = args[0]
	razl = 0
	for i in range((len(string) // 2)):
	    if (string[i] != string[((- i) - 1)]):
	        razl += 1
	if (razl > 1):
	    ret_values.append('NO')
	elif (razl == 1):
	    ret_values.append('YES')
	elif ((len(string) % 2) == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
