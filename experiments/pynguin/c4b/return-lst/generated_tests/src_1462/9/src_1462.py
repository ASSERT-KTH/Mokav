def func(*args):
	ret_values = []
	
	string = args[0]
	list1 = []
	num1 = '47'
	for i in string:
	    if (i in num1):
	        list1.append(i)
	        continue
	    elif (i not in num1):
	        break
	if (len(list1) != len(string)):
	    if (((int(string) % 4) == 0) or ((int(string) % 7) == 0) or ((int(string) % 47) == 0)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
