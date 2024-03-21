def func(*args):
	ret_values = []
	
	username = args[0]
	num = 0
	for i in range(len(username)):
	    for a in range(0, i):
	        if (username[i] == username[a]):
	            num -= 1
	            break
	    num += 1
	if ((num % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
