def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = list(str(n))
	c = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        c = (c + 1)
	if (((n % 4) == 0) or ((n % 7) == 0) or ((n % 47) == 0)):
	    ret_values.append('YES')
	elif (c == len(s)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
