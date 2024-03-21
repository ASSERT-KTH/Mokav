def func(*args):
	ret_values = []
	
	n = int(args[0])
	flag = False
	not_lucky = False
	s = str(n)
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        pass
	    else:
	        not_lucky = True
	        break
	if (not not_lucky):
	    flag = True
	if flag:
	    ret_values.append('YES')
	elif ((n % 47) == 0):
	    ret_values.append('YES')
	elif ((n % 4) == 0):
	    ret_values.append('YES')
	elif ((n % 7) == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
